import requests
import unittest
from dataclasses import asdict

from static_data.majors_list import ALL_MAJORS
from api.models.account import Account
from api.tests.dummy_data import USER_1
from api.tests.base_test import BaseTestCase


class MajorTest(BaseTestCase):
    
    def setUp(self):     
        self.base_setUp()
        
    # GET /majors
    def test_add_user(self):
        ENDPOINT = "majors"
        
        response = requests.get(self.BASE_URL + ENDPOINT, headers=self.HEADERS)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        majors_list = response_data['majors']
        
        
        count = 0
        for major in majors_list:
            level = major[1]
            name = major[2]
            self.assertIn((level, name), ALL_MAJORS, msg=f"{(level, name)} not in list of majors")
            count += 1
            
        self.assertEqual(count, len(ALL_MAJORS))
        
        
    def tearDown(self):
        self.base_tearDown()

if __name__ == '__main__':
    unittest.main()