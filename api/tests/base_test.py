import requests
import unittest
from dataclasses import asdict

from api.planetscale_connection import get_db_session
from api.queries import Database


class BaseTestCase(unittest.TestCase):
    
    BASE_URL = "http://127.0.0.1:5000/"
    
    def base_setUp(self):     
        self.session = get_db_session(autocommit=True)
        self.db = Database(self.session)
        
    def base_tearDown(self):
        self.session.close()

