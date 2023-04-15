from sqlalchemy import select
from sqlalchemy.orm import Session

from api.models.account import Account
from api.models.major import Major

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
        