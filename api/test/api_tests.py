import json
import requests
import unittest

from api.test.dummy_data import USER_1

class APITestCase(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"

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
        
        response = requests.post(self.BASE_URL + endpoint, json=data)
        self.assertEqual(response.status_code, 200)
        
    

if __name__ == '__main__':
    unittest.main()