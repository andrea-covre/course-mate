import requests
import unittest
from dataclasses import asdict

from static_data.majors_list import ALL_MAJORS
from api.tests.dummy_data import SECTION_1, CLASS_1
from api.tests.base_test import BaseTestCase
from api.models.section import Section
from api.models.schedule import Schedule
from api.models.class_ import Class

user_id = 0

class ScheduleTest(BaseTestCase):
    
    def setUp(self):     
        self.base_setUp()
        
        # Delete dummy section from database
        self.session.query(Section).filter(
            (Section.crn == SECTION_1.crn)).delete()
        
        # Delete dummy class from database
        self.session.query(Class).filter(
            (Class.subject_code == CLASS_1.subject_code and 
             Class.class_code == CLASS_1.class_code)).delete()
        
        # Add dummy class to database
        dummy_class = Class(asdict(CLASS_1))
        self.session.add(dummy_class)
        self.session.commit()
        
        CLASS_1.id = dummy_class.id
        SECTION_1.class_id = CLASS_1.id
        
        # Add dummy section to database
        dummy_section = Section(asdict(SECTION_1))
        self.session.add(dummy_section)
        self.session.commit()
        
        SECTION_1.id = dummy_section.section_id
        
    # GET /schedule/add
    def test_add_section_by_crn(self):
        ENDPOINT = "schedule/add"
        
        section_data = {
            "user_id": user_id,
            "semester_id": SECTION_1.semester_id,
            "crn": SECTION_1.crn,
        }
        
        # Testing endpoint
        response = requests.post(self.BASE_URL + ENDPOINT, json=section_data, headers=self.HEADERS)
        self.assertEqual(response.status_code, 200)
        
        # Verifying schedule entry was added
        entry = self.db.get_schedule_entry(user_id=user_id, section_id=SECTION_1.id)
        if not entry:
            self.fail("Schedule entry not added")
        
        
    def test_add_section_by_section_info(self):
        ENDPOINT = "schedule/add"
    
        section_data = {
            "user_id": user_id,
            "semester_id": SECTION_1.semester_id,        
            "subject_code": CLASS_1.subject_code,
            "class_number": CLASS_1.class_code,
            "section_code": SECTION_1.section_code
        }
        
        # Testing endpoint
        response = requests.post(self.BASE_URL + ENDPOINT, json=section_data, headers=self.HEADERS)
        self.assertEqual(response.status_code, 200)
        
        # Verifying schedule entry was added
        entry = self.db.get_schedule_entry(user_id=user_id, section_id=SECTION_1.id)
        if not entry:
            self.fail("Schedule entry not added")
    
    
    # def test_get_user_schedule(self):
    #     x = self.db.get_user_schedule(304, 202308)
    #     return x
        
    def tearDown(self):
        # Delete dummy section from database
        self.session.query(Section).filter(
            (Section.crn == SECTION_1.crn)).delete()
        self.session.commit()
        
        # Delete dummy section from database
        self.session.query(Class).filter(
            (Class.id == CLASS_1.id)).delete()
        self.session.commit()
        
        # Delete dummy entry 
        self.session.query(Schedule).filter(
            (Schedule.account_id == user_id and Schedule.section_id == SECTION_1.id)).delete()
        
        self.base_tearDown()

if __name__ == '__main__':
    unittest.main()