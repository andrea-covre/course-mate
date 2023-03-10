import textwrap
import pyodbc
from account import Account
from connection import SQLConnectionObject

VALID = 1
INVALID = 0

class SQLOperations:
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
    
    def create_account(self, id, email_address, edu_email_address, first_name, last_name, phone_number, grad_year, major_id, firebase_id):
        cnxn, crsr = self.connection.open_connection()
        query = "SET IDENTITY_INSERT [account] ON\
                INSERT INTO [account]\
                (id, email_address, edu_email_address, first_name, last_name, phone_number, grad_year, major_id, firebase_id)\
                VALUES ({id}, '{email_address}', '{edu_email_address}', '{first_name}', '{last_name}', {phone_number}, {grad_year}, {major_id}, '{firebase_id}')\
                SET IDENTITY_INSERT [account] OFF".format(
                    id = id,
                    email_address=email_address,
                    edu_email_address=edu_email_address,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    grad_year=grad_year,
                    major_id=major_id,
                    firebase_id = firebase_id
                )
        print(query)
        crsr.execute(query)
        crsr.commit()
        cnxn.close()
    
    def update_account_email_address(self, id, email_address): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET email_address = '{value}'\
        WHERE ID = {id}".format(
            value = email_address,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()

    def update_account_edu_email_address(self, id, edu_email_address): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET edu_email_address = '{value}'\
        WHERE ID = {id}".format(
            value = edu_email_address,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()
    
    def update_account_first_name(self, id, first_name): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET first_name = '{value}'\
        WHERE ID = {id}".format(
            value = first_name,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()

    def update_account_last_name(self, id, last_name): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET last_name = '{value}'\
        WHERE ID = {id}".format(
            value = last_name,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()
    
    def update_account_phone_number(self, id, phone_number): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET phone_number = '{value}'\
        WHERE ID = {id}".format(
            value = phone_number,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()

    def update_account_major_id(self, id, major_id): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET major_id = {value}\
        WHERE ID = {id}".format(
            value = major_id,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()

    def update_account_grad_year(self, id, grad_year): 
        cnxn, crsr = self.connection.open_connection()
        query = "UPDATE [account]\
        SET grad_year = {value}\
        WHERE ID = {id}".format(
            value = grad_year,
            id = id
        )
        crsr.execute(query)
        crsr.commit()
        cnxn.close()

if __name__ == "__main__":
    obj = SQLOperations()
    obj.update_account_by_id(2, {'email_address': "test@gmail.com"})

def parse_from_response(response) -> Account:
    print(response)
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
        firebase_id = response[8]
        account = Account(id, email_address, first_name, last_name, grad_year, major_id, phone_number, edu_email_address, firebase_id)
        return account
    else:
        return INVALID
