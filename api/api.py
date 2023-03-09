import textwrap
import pyodbc
import json 
import datetime
import ast
import requests

from account import Account
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from connection import SQLConnectionObject
from database import SQLOperations, parse_from_response

app = Flask(__name__)
api = Api(app)

#Example = /users?id=<user_id>
@app.route('/users', methods=['GET'])
def users():
    args = request.args
    print(json.dumps(args))
    id = args.get('id')
    operations = SQLOperations()
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400

@app.route('/users/add', methods=['POST'])
def testpost():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data['id']
    email_address = data['email_address']
    first_name = data['first_name']
    last_name = data['last_name']
    major_id = data['major_id']

    edu_email_address = None
    phone_number = None
    grad_year = None
    firebase_id = None

    if 'edu_email_address' in data:
        edu_email_address = data['edu_email_address']
    if 'phone_number' in data:
        phone_number = data['phone_number']
    if 'grad_year' in data:
        grad_year = data['grad_year']
    if 'firebase_id' in data:
        firebase_id = data['firebase_id']

    operations = SQLOperations()
    operations.create_account(id, email_address, edu_email_address, first_name, last_name,
                            phone_number, grad_year, major_id, firebase_id)
    
    return jsonify(data)
    

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
