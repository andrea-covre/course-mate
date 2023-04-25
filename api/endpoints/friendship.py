from flask import Blueprint, request

from api.resources import db
from api.models.friendship import Status

ROUTE_PREFIX = '/friendship'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)

    
# GET /request?sender_id=<sender_id>&receiver_id=<receiver_id>
@blueprint.route('/request', methods=['GET'])
def request_friendship():
    args = request.args
    sender_id = args.get('sender_id')
    receiver_id = args.get('receiver_id')
    
    if sender_id == receiver_id:
        return {'Message': 'sender_id and receiver_id are the same user'}, 400
    
    friendship = db.get_friendship(sender_id, receiver_id)
    
    if friendship:
        if friendship.status == Status.accepted:
            return {'Message': f'User {sender_id} and user {receiver_id} are already friends.'}, 409
        
        if sender_id == friendship.account_id_1:
            return {'Message': f'User {sender_id} has already requested a friendship with user {receiver_id}.'}, 409
        
        if sender_id == friendship.account_id_2:
            db.accept_friendship(receiver_id, sender_id)
            return {'Message': f'Pending friendship request with user {receiver_id} accepted'}, 200
    
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

# DELETE /delete?user1_id=<sender_id>&user2_id=<receiver_id>
@blueprint.route('/delete', methods=['DELETE'])
def delete_friendship():
    args = request.args
    user1_id = args.get('user1_id')
    user2_id = args.get('user2_id')
    
    db.delete_friendship(user1_id, user2_id)
    
    return {}, 200

# GET /list?user_id=<user_id>
@blueprint.route('/list', methods=['GET'])
def get_all_friendships():
    args = request.args
    user_id = args.get('user_id')
    
    friendships = db.get_all_friendships(user_id)
    
    return friendships, 200

# GET /get_by_section?user_id=<user_id>&section_id=<section_id>
@blueprint.route('/get_by_section', methods=['GET'])
def get_friendships_by_section():
    args = request.args
    user_id = args.get('user_id')
    section_id = args.get('section_id')
    
    friendships = db.get_friendships_by_section(user_id, section_id)
    
    return friendships, 200
