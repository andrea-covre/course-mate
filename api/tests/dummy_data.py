from dataclasses import dataclass

@dataclass
class DummyUser():
    email_address: str
    edu_email_address: str
    first_name: str
    last_name: str
    phone_number: int
    grad_year: int
    major_id: int
    
USER_1 = DummyUser(
    email_address = "andy@coursemate.com",
    edu_email_address = "andy@gt.edu",
    first_name = "Andy",
    last_name = "Cobra",
    phone_number = 9999999999,
    grad_year = 2024,
    major_id = 54
)