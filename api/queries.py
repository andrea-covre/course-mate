from sqlalchemy import select
from sqlalchemy.orm import Session

from api.models.account import Account

class Database():
    def __init__(self, session: Session, commit_to_remote: bool = True):
        self.session = session
        self.commit_to_remote = commit_to_remote
        
    def get_account_by_id(self, id: int) -> Account:
        stmt = select(Account).where(
            Account.id.in_([id])
        )
        account = self.session.scalar(stmt)
        return account
        
    def add_account(self, account_data: dict) -> int:
        new_account = Account(account_data)
        self.session.add(new_account)
        self._commit()
        return new_account.id
    
    def delete_account(self, account: Account):
        self.session.delete(account)
        self._commit()
        
    def _commit(self):
        if self.commit_to_remote:
            self.session.commit()