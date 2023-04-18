from flask import Blueprint, request

from api.resources import db
from api.utils import load_request_data

ROUTE_PREFIX = '/friendship'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)

    
# GET /request?sender_id=<sender_id>&receiver_id=<receiver_id>
@blueprint.route('/request', methods=['GET'])
def request_friendship():
    args = request.args
    sender_id = args.get('sender_id')
    receiver_id = args.get('receiver_id')
    
    db.request_friendship(sender_id, receiver_id)
    
    return {}, 200

# GET /accept?sender_id=<sender_id>&receiver_id=<receiver_id>
@blueprint.route('/accept', methods=['GET'])
def accept_friendship():
    args = request.args
    sender_id = args.get('sender_id')
    receiver_id = args.get('receiver_id')
    
    db.accept_friendship(sender_id, receiver_id)
    
    return {}, 200

# GET /delete?user1_id=<sender_id>&user2_id=<receiver_id>
@blueprint.route('/delete', methods=['GET'])
def delete_friendship():
    args = request.args
    user1_id = args.get('user1_id')
    user2_id = args.get('user2_id')
    
    db.delete_friendship(user1_id, user2_id)
    
    return {}, 200

# GET /list?user_id=<user_id>
@blueprint.route('/list', methods=['GET'])
def get_friendships():
    args = request.args
    user_id = args.get('user_id')
    
    friendships = db.get_friendships(user_id)
    
    return friendships, 200

# GET /get_by_section?user_id=<user_id>&section_id=<section_id>
@blueprint.route('/get_by_section', methods=['GET'])
def get_friendships_by_section():
    args = request.args
    user_id = args.get('user_id')
    section_id = args.get('section_id')
    
    friendships = db.get_friendships_by_section(user_id, section_id)
    
    return friendships, 200

    
