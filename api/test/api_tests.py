import json
import requests
import unittest

from api.planetscale_connection import get_db_session
from api.models.account import Account
from api.test.dummy_data import USER_1

BASE_URL = "http://127.0.0.1:5000/"

class AccountTest(unittest.TestCase):
    
    def setUp(self):
        self.session = get_db_session()
        
        # Making sure DUMMY USER 1 is not in the database already, if so delete it
        self.session.query(Account).filter(
            (Account.email_address == USER_1.email_address) |
            (Account.email_address == USER_1.edu_email_address) |
            (Account.phone_number == USER_1.phone_number)
        ).delete()
        self.session.commit()


    def test_add_user(self):
        """
        Target: POST /users/add
        """
        endpoint = "users/add"
        data = {
            "email_address": USER_1.email_address,
            "edu_email_address": USER_1.edu_email_address,
            "first_name": USER_1.first_name,
            "last_name": USER_1.last_name,
            "phone_number": USER_1.phone_number,
            "grad_year": USER_1.grad_year,
            "major_id": USER_1.major_id
            }
        
        response = requests.post(BASE_URL + endpoint, json=data)
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        USER_1.id = response_data[Account.id.name]
        
    # def test_get_user(self):
    #     """
    #     Target: GET /users?id=<user_id>
    #     """
        
    

if __name__ == '__main__':
    unittest.main()