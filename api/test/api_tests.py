import json
import requests
import unittest

from dataclasses import asdict

from api.planetscale_connection import get_db_session
from api.models.account import Account
from api.test.dummy_data import USER_1
from api.queries import Database

COMMIT_TO_REMOTE = True
BASE_URL = "http://127.0.0.1:5000/"

class AccountTest(unittest.TestCase):
    
    def setUp(self):
        self.session = get_db_session()
        self.db = Database(self.session, commit_to_remote=COMMIT_TO_REMOTE)
        
        # Making sure DUMMY USER 1 is not in the database already, if so delete it
        self.session.query(Account).filter(
            (Account.email_address == USER_1.email_address) |
            (Account.email_address == USER_1.edu_email_address) |
            (Account.phone_number == USER_1.phone_number)
        ).delete()
        self.db._commit()

    def test_add_user(self):
        """
        Target: POST /users/add
        """
        endpoint = "users/add"
        
        user_data = asdict(USER_1)
        
        # Adding user to database
        response = requests.post(BASE_URL + endpoint, json=user_data)
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        new_user_id = response_data[Account.id.name] 
        
        user = self.db.get_account_by_id(new_user_id)
        print(dict(user))
        
        exit()
        
        
        # Verifying that the user was added to the database
        
        
        
    def test_get_user(self):
        """
        Target: GET /users
        """
        endpoint = "users"
        params = {'id': USER_1.id}
        response = requests.get(BASE_URL + endpoint, params=params)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data[Account.id.name], USER_1.id)
        self.assertEqual(response_data[Account.email_address.name], USER_1.email_address)
        self.assertEqual(response_data[Account.edu_email_address.name], USER_1.edu_email_address)
        self.assertEqual(response_data[Account.first_name.name], USER_1.first_name)
        self.assertEqual(response_data[Account.last_name.name], USER_1.last_name)
        self.assertEqual(response_data[Account.phone_number.name], USER_1.phone_number)
        self.assertEqual(response_data[Account.grad_year.name], USER_1.grad_year)
        self.assertEqual(response_data[Account.major_id.name], USER_1.major_id)
        
    def test_delete_user(self):
        """
        Target: DELETE /users/delete/<user_id>
        """
        endpoint = f"users/delete/{USER_1.id}"
        response = requests.delete(BASE_URL + endpoint)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['Code'], 200)
        self.assertEqual(response_data['Message'], f'User with ID {USER_1.id} deleted successfully.')
        
        # Verify that the user has been deleted from the database
        deleted_user = self.session.query(Account).filter(Account.id == USER_1.id).first()
        self.assertIsNone(deleted_user)
        
    def tearDown(self):
        if not COMMIT_TO_REMOTE:
            self.session.rollback()
            
        self.session.close()

if __name__ == '__main__':
    unittest.main()