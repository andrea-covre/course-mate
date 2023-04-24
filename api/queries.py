from typing import Tuple

from sqlalchemy import select, or_, and_
from sqlalchemy.orm import Session, aliased

from api.models.major import Major
from api.models.class_ import Class
from api.models.section import Section
from api.models.account import Account
from api.models.schedule import Schedule
from api.models.semester import Semester
from api.models.friendship import Friendship, Status
from api.planetscale_connection import get_db_session


class Database():
    def __init__(self):
        self.session = get_db_session(autocommit=True)
        
    def close(self):
        self.session.close()
        
    def renew_session(self):
        self.session.close()
        self.session = get_db_session(autocommit=True)
        
    def get_account_by_id(self, id: int) -> Account:
        stmt = select(Account).where(Account.id == id)
        account = self.session.scalar(stmt)
        return account
    
    def get_account_by_phone_number(self, phone_number) -> Account:
        stmt = select(Account).where(Account.phone_number == phone_number)
        account = self.session.scalar(stmt)
        return account
    
    def get_account_by_email(self, email) -> Account:
        stmt = select(Account).where(Account.email_address == email)
        account = self.session.scalar(stmt)
        return account
    
    def get_account_by_edu_email(self, edu_email) -> Account:
        stmt = select(Account).where(Account.edu_email_address == edu_email)
        account = self.session.scalar(stmt)
        return account
    
    def get_account_by_name(self, first_name, last_name) -> Account:
        stmt = select(Account).where(and_(Account.first_name == first_name, Account.last_name == last_name))
        account = self.session.scalar(stmt)
        return account
        
    def add_account(self, account_data: dict) -> int:
        new_account = Account(account_data)
        self.session.add(new_account)
        self.session.commit()
        return new_account.id
    
    def delete_account(self, account: Account):
        self.session.delete(account)
        self.session.commit()
        
    def get_majors(self):
        stmt = select(Major)
        majors_list = self.session.execute(stmt).all()
        majors = []
        for major in majors_list:
            major = major[0].as_dict()
            id = major['id']
            level = major['level']
            name = major['name']
            majors.append([id, level, name])
        return majors
    
    def get_section_id_by_crn(self, semester, crn):
        stmt = select(Section.section_id).where(
            Section.crn == crn and 
            Section.semester_id == semester)
        section_id = self.session.scalar(stmt)
        return section_id
    
    def get_section_id_by_class_id(self, semester, class_id, section_code):   
        stmt = select(Section.section_id).where(
            Section.class_id == class_id and
            Section.semester_id == semester and
            Section.section_code == section_code)
        section_id = self.session.scalar(stmt)
        return section_id
    
    def get_class_id(self, subject_code, class_number):
        stmt = select(Class.id).where(
            Class.subject_code == subject_code and 
            Section.class_code == class_number)
        class_id = self.session.scalar(stmt)
        return class_id
    
    def add_schedule_entry(self, user_id, section_id):
        entry_data = {
            "account_id": user_id,
            "section_id": section_id
        }        
        new_entry = Schedule(entry_data)
        self.session.add(new_entry)
        self.session.commit()   
        
    def get_schedule_entry(self, user_id, section_id):
        stmt = select(Schedule).where(Schedule.account_id == user_id and Schedule.section_id == section_id)
        entry = self.session.scalar(stmt)
        return entry
        
    
    def get_user_schedule(self, user_id, semester_id):
        query = (
            select(
                Class.title,
                Class.subject_code,
                Class.class_code,
                Section.section_code,
                Section.crn,
                Section.section_id
            )
            .select_from(Schedule)
            .join(Section, Schedule.section_id == Section.section_id)
            .join(Class, Section.class_id == Class.id)
            .where(
                Schedule.account_id == user_id,
                Section.semester_id == semester_id
            )
        )
        results = self.session.execute(query)
        schedule = []
        for row in results:
            title, subject_code, class_code, section_code, crn, section_id = row
            schedule.append({
                "title": title,
                "subject_code": subject_code,
                "class_code": class_code,
                "section_code": section_code,
                "crn": crn,
                "section_id": section_id
            })
            
        return schedule
    
    
    def get_common_schedule(self, user_1_id, user_2_id, semester_id):
        s1 = aliased(Schedule)
        s2 = aliased(Schedule)
        query = (
            select(
                Class.title,
                Class.subject_code,
                Class.class_code,
                Section.section_code,
                Section.crn,
                Section.section_id
            )
            .select_from(s1)
            .join(s2, s1.section_id == s2.section_id and s1.account_id != s2.account_id)
            .join(Section, s1.section_id == Section.section_id)
            .join(Class, Section.class_id == Class.id)
            .where(
                (s1.account_id == user_1_id) &
                (s2.account_id == user_2_id) &
                (Section.semester_id == semester_id)
            )
        )
        
        results = self.session.execute(query)
            
        schedule = []
        for row in results:
            title, subject_code, class_code, section_code, crn, section_id = row
            schedule.append({
                "title": title,
                "subject_code": subject_code,
                "class_code": class_code,
                "section_code": section_code,
                "crn": crn,
                "section_id": section_id
            })
            
        return schedule
    
    
    def request_friendship(self, sender_id, receiver_id):
        new_entry = {
            "account_id_1": sender_id,
            "account_id_2": receiver_id,
            "status": Status.pending
        }
        new_friendship = Friendship(new_entry)
        self.session.add(new_friendship)
        self.session.commit()
        
        
    def accept_friendship(self, sender_id, receiver_id):
        stmt = select(Friendship).where(
        Friendship.account_id_1.in_([sender_id]) 
            ).where(
                Friendship.account_id_2.in_([receiver_id]) 
            )
        for obj in self.session.scalars(stmt):
            friendship_object = obj
        friendship_object.status = Status.accepted
        self.session.commit()
        
        
    def delete_friendship(self, user1_id, user2_id):
        stmt = select(Friendship).where(
            or_(
                and_(
                    Friendship.account_id_1 == user1_id, 
                    Friendship.account_id_2 == user2_id
                    ),
                and_(
                    Friendship.account_id_1 == user2_id,
                    Friendship.account_id_2 == user1_id
                    )
            ))
        friendship = self.session.scalar(stmt)
        self.session.delete(friendship)
        self.session.commit()
        
        
    def get_friendships(self, user_id):
        # Getting all friendships
        stmt = select(Friendship).where(
            or_(Friendship.account_id_1 == user_id, Friendship.account_id_2 == user_id))
        friendships = self.session.execute(stmt).all()
        
        accepted = []
        outgoing = []
        incoming = []
        
        for friendship in friendships:
            friendship = friendship[0].as_dict()
            sender_id = friendship['account_id_1']
            receiver_id = friendship['account_id_2']
            
            if friendship['status'] == Status.accepted:
                if sender_id == user_id:
                    accepted.append(receiver_id)
                else:
                    accepted.append(sender_id)
            else:
                if sender_id == user_id:
                    outgoing.append(receiver_id)
                else:
                    incoming.append(sender_id)

        friendships = {
            "friends": accepted,
            "outgoing_requests": outgoing,
            "incoming_requests": incoming
        }
        
        return friendships
    
    
    def get_friendships_by_section(self, user_id, section_id):
        accounts = (self.session.query(Account).distinct().
            join(Friendship, ((Account.id == Friendship.account_id_2) | (Account.id == Friendship.account_id_1))).
            join(Schedule, Account.id == Schedule.account_id).
            filter(((Friendship.account_id_1 == user_id) | (Friendship.account_id_2 == user_id)), 
                (Friendship.status == 'accepted'),
                (Schedule.section_id == section_id),
                (Account.id != user_id)).all())
            
        friends = []
        for account in accounts:
            account = account.as_dict()
            friends.append({
                    'first_name': account['first_name'],
                    'last_name': account['last_name'],
                    'id': account['id'],
                })
            
        return friends
    
    def get_semesters(self):
        results = self.session.query(Semester).all()
        semesters = []
        for semester in results:
            semester = semester.as_dict()
            semesters.append(semester)
        return semesters
        

        
        