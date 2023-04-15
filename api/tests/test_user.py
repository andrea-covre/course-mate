import requests
import unittest
from dataclasses import asdict

from sqlalchemy import select

from api.planetscale_connection import get_db_session
from api.models.account import Account
from api.tests.dummy_data import USER_1
from api.queries import Database
from api.tests.base_test import BaseTestCase


class AccountTest(BaseTestCase):
    
    def setUp(self):     
        self.base_setUp()
        
        # Making sure DUMMY USER 1 is not in the database already, if so delete it
        self.session.query(Account).filter(
            (Account.email_address == USER_1.email_address) |
            (Account.email_address == USER_1.edu_email_address) |
            (Account.phone_number == USER_1.phone_number)
        ).delete()
        
    # POST /users/add
    def test_add_user(self):
        ENDPOINT = "users/add"
        
        user_data = asdict(USER_1)
        
        # Adding user to database using the API
        response = requests.post(self.BASE_URL + ENDPOINT, json=user_data)
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        new_user_id = response_data[Account.id.name] 
        
        # Verifying insertion directly from database
        inserted_user = self.db.get_account_by_id(new_user_id)
        inserted_user_data = inserted_user.as_dict()
        inserted_user_data.pop(Account.id.name)
        
        self.assertDictEqual(user_data, inserted_user_data)
        
    # GET /users?id=<user_id>
    def test_get_user(self):
        ENDPOINT = "users"
        
        # Add user directly through the database
        user_id = self.db.add_account(asdict(USER_1))
        params = {'id': user_id}
        
        # Getting just added user through the API
        response = requests.get(self.BASE_URL + ENDPOINT, params=params)
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        response_data.pop(Account.id.name)

        self.assertDictEqual(response_data, asdict(USER_1))
        
    # DELETE /users/delete?id=<user_id>
    def test_delete_user(self):
        ENDPOINT = f"users/delete"
        
        # Add user directly through the database
        account_id_to_delete = self.db.add_account(asdict(USER_1))
          
        # Delete user through the API
        params = {'id': account_id_to_delete}
        response = requests.delete(self.BASE_URL + ENDPOINT, params=params)
    
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertEqual(response_data['Code'], 200)
        self.assertEqual(response_data['Message'], f'User with ID {account_id_to_delete} deleted successfully.')
        
        # Verify that the user has been deleted directly from the database
        inserted_user = self.db.get_account_by_id(account_id_to_delete)
        self.assertIsNone(inserted_user)
        
    def tearDown(self):
        self.base_tearDown()

if __name__ == '__main__':
    unittest.main()