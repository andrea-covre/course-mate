class Account:
    def __init__(self, id, email_address, first_name, last_name, grad_year, major_id, phone_number = None, edu_email_address = None, firebase_id = None):
        self.id = id
        self.email_address = email_address
        self.edu_email_address = edu_email_address
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.grad_year = grad_year
        self.major_id = major_id
        self.firebase_id = firebase_id
    

    

