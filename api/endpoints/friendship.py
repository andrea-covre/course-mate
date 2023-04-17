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

# GET /delete?sender_id=<sender_id>&receiver_id=<receiver_id>
@blueprint.route('/delete', methods=['GET'])
def delete_friendship():
    args = request.args
    sender_id = args.get('sender_id')
    receiver_id = args.get('receiver_id')
    
    db.delete_friendship(sender_id, receiver_id)
    
    return {}, 200

    
