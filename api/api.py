import textwrap
import pyodbc
import json 
import datetime
from account import Account
from connection import SQLConnectionObject

VALID = 1
INVALID = 0

class API:
    def __init__(self):
        self.connection = SQLConnectionObject()

    def get_account_by_id(self, id: int) -> Account:
        cnxn, crsr = self.connection.open_connection()
        query = "SELECT * FROM [account] WHERE ID = {id}".format(id=id)
        crsr.execute(query)
        response = crsr.fetchall()
        account = parse_from_response(response)
        cnxn.close()
        return account
    
    def create_account(self, id, email_address, edu_email_address, first_name, last_name, phone_number, grad_year, major_id):
        cnxn, crsr = self.connection.open_connection()
        query = "SET IDENTITY_INSERT [account] ON\
                INSERT INTO [account]\
                (id, email_address, edu_email_address, first_name, last_name, phone_number, grad_year, major_id)\
                VALUES ({id}, '{email_address}', '{edu_email_address}', '{first_name}', '{last_name}', '{phone_number}', {grad_year}, {major_id})\
                SET IDENTITY_INSERT [account] OFF".format(
                    id = id,
                    email_address=email_address,
                    edu_email_address=edu_email_address,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    grad_year=grad_year,
                    major_id=major_id
                )
        
        crsr.execute(query)
        crsr.commit()
        cnxn.close()
    

def parse_from_response(self, response) -> Account:
    if response:
        response = response[0]
        id = response[0]
        email_address = response[1]
        edu_email_address = response[2]
        first_name = response[3]
        last_name = response[4]
        phone_number = response[5]
        grad_year = response[6]
        major_id = response[7]
        account = Account(id, email_address, edu_email_address, first_name, last_name, phone_number, grad_year, major_id)
        return account
    else:
        return INVALID



def main():
    api = API()
    # api.get_account_by_id(id = 3)
    # api.create_account()

if __name__ == "__main__":
    main()