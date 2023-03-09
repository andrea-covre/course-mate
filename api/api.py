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
#Example = Create a post request with "/users/add" appended to the API url
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
    
@app.route('/users/update/email', methods=['PUT'])
def update_email():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    email_address = data["email_address"]
    operations = SQLOperations()
    operations.update_account_email_address(id, email_address)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400

@app.route('/users/update/edu_email', methods=['PUT'])
def update_edu_email():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    edu_email_address = data["edu_email_address"]
    operations = SQLOperations()
    operations.update_account_edu_email_address(id, edu_email_address)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400

@app.route('/users/update/first_name', methods=['PUT'])
def update_first_name():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    first_name = data["first_name"]
    operations = SQLOperations()
    operations.update_account_first_name(id, first_name)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400


@app.route('/users/update/last_name', methods=['PUT'])
def update_last_name():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    last_name = data["last_name"]
    operations = SQLOperations()
    operations.update_account_last_name(id, last_name)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400

@app.route('/users/update/phone_number', methods=['PUT'])
def update_phone_number():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    phone_number = data["phone_number"]
    operations = SQLOperations()
    operations.update_account_phone_number(id, phone_number)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400
    
@app.route('/users/update/major_id', methods=['PUT'])
def update_major_id():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    major_id = data["major_id"]
    operations = SQLOperations()
    operations.update_account_phone_number(id, major_id)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400

@app.route('/users/update/grad_year', methods=['PUT'])
def update_grad_year():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data["id"]
    grad_year = data["grad_year"]
    operations = SQLOperations()
    operations.update_account_phone_number(id, grad_year)
    result = operations.get_account_by_id(id)
    if result:
        return result.__dict__, 200
    else:
        return {}, 400
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
