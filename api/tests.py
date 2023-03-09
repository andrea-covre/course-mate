import requests
import json 
from flask import jsonify

url = "http://127.0.0.1:5000/post"
obj = {
    "id": 10,
    "edu_email_address": None,
    "email_address": "pranav.thomas76@gmail.com",
    "firebase_id": None,
    "first_name": "pthomas76@gatech.edu",
    "grad_year": 2023,
    "last_name": "Pranav",
    "major_id": 3,
    "phone_number": "4048616170"
}
x = requests.post(url, json = json.dumps(obj))
print(x.text)

url = "http://127.0.0.1:5000/users/update/email"
obj = {
    "id": 10,
    "email_address": "test2@gmail.com"
}
x = requests.put(url, json = json.dumps(obj))
print(x.text)