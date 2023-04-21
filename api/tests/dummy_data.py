from dataclasses import dataclass

from api.models.account import Account

@dataclass
class DummyUser():
    id: str
    email_address: str
    edu_email_address: str
    first_name: str
    last_name: str
    phone_number: int
    grad_year: int
    major_id: int
    
USER_1 = DummyUser(
    id = "00010101000",
    email_address = "andy@coursemate.com",
    edu_email_address = "andy@gt.edu",
    first_name = "test_name",
    last_name = "test_lastname",
    phone_number = 9999999999,
    grad_year = 2024,
    major_id = 54
)


@dataclass
class DummySection():
    title: str
    semester_id: int
    class_id: int
    crn: int
    section_code: str
    location_id: int
    credits: int
    levels: str
    grade_basis: str
    campus: str
    
SECTION_1 = DummySection(
    title = "test_section",
    semester_id = 900000,
    class_id = None,
    crn = 99999,
    section_code = "TST",
    location_id = 0,
    credits = 0,
    levels = "test",
    grade_basis = "TTT",
    campus = "test"
)


@dataclass
class DummyClass():
    title: str
    subject_code: str
    class_code: str
    
CLASS_1 = DummyClass(
    title = "test_class",
    subject_code = "CS",
    class_code = "0001"
)

def delete_dummy_user(session, dummy_user: DummyUser):
    session.query(Account).filter(
        (Account.email_address == dummy_user.email_address) |
        (Account.email_address == dummy_user.edu_email_address) |
        (Account.phone_number == dummy_user.phone_number)
    ).delete()
    