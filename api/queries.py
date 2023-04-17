from typing import Tuple

from sqlalchemy import select
from sqlalchemy.orm import Session, aliased

from api.models.account import Account
from api.models.major import Major
from api.models.section import Section
from api.models.schedule import Schedule
from api.models.class_ import Class


class Database():
    def __init__(self, session: Session):
        self.session = session
        
    def get_account_by_id(self, id: int) -> Account:
        stmt = select(Account).where(Account.id == id)
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
            schedule.append((title, subject_code, class_code, section_code, crn, section_id))
            
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
            schedule.append((title, subject_code, class_code, section_code, crn, section_id))
            
        return schedule
    
