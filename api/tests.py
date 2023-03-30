import requests
import json 
from flask import jsonify

url = "http://127.0.0.1:5000/users/update"
obj = {
    "id": 1,
    "first_name": "Pranav",
    "last_name": "Thomas", 
    "grad_year": 2024,
}
x = requests.put(url, json = json.dumps(obj))
print(x.text)

# url = "http://127.0.0.1:5000/users/update/email"
# obj = {
#     "id": 10,
#     "email_address": "test2@gmail.com"
# }
# x = requests.put(url, json = json.dumps(obj))
# print(x.text)