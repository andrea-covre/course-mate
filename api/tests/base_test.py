import requests
import unittest
from dataclasses import asdict

import os

from dotenv import load_dotenv

from api.queries import Database

load_dotenv()

class BaseTestCase(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    HEADERS = {'Authorization': os.getenv("API_TOKEN_PLAINTEXT")}
    
    def base_setUp(self):     
        self.db = Database()
        
    def base_tearDown(self):
        self.db.close()

