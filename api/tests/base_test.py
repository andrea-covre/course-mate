import requests
import unittest
from dataclasses import asdict

import os

from dotenv import load_dotenv

from api.queries import Database
from api.planetscale_connection import get_db_session

load_dotenv()

class BaseTestCase(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    HEADERS = {'Authorization': os.getenv("API_TOKEN_PLAINTEXT")}
    
    def base_setUp(self):     
        self.session = get_db_session(autocommit=True)
        self.db = Database(self.session)
        
    def base_tearDown(self):
        self.session.close()

