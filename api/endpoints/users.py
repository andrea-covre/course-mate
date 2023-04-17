from flask import Blueprint, request

from api.resources import db
from api.utils import load_request_data

ROUTE_PREFIX = '/users'

users_blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)

# GET /users?id=<user_id>
@users_blueprint.route('', methods=['GET'])
def users():
    args = request.args
    id = args.get('id')
    user = db.get_account_by_id(id)
    if user:
        return user.as_dict(), 200
    else:
        return {}, 404
    
    
# POST /users/add
@users_blueprint.route('/add', methods=['POST'])
def add_user():
    data = request.get_json(force=True)
    data = load_request_data(data)
    new_account_id = db.add_account(data)
    return {'Code': 200, 'id': new_account_id}


# DELETE /users/delete?id=<user_id>
@users_blueprint.route('/delete', methods=['DELETE'])
def delete_user():
    args = request.args
    id = args.get('id')
    user_to_delete = db.get_account_by_id(id)
    
    if user_to_delete is not None:
        db.delete_account(user_to_delete)
        return {'Code': 200, 'Message': f'User with ID {id} deleted successfully.'}
    else:
        return {'Code': 404, 'Message': f'User with ID {id} not found.'}
    
