import json 
from flask import Flask, request, jsonify
from flask_restful import Api
from planetscale_connection import get_db_session
from models import major
from models import account
from sqlalchemy import select
from sqlalchemy.orm import Session

session = get_db_session()
app = Flask(__name__)
api = Api(app)

#Example = /users?id=<user_id>
@app.route('/users', methods=['GET'])
def users():
    args = request.args
    id = args.get('id')
    stmt = select(account.Account).where(
        account.Account.id.in_([id])
    )
    results = session.scalar(stmt)
    if not results:
        return {}, 200
    else:
        return results.as_dict(), 200
    
#Example = Create a post request with "/users/add" appended to the API url
@app.route('/users/add', methods=['POST'])
def testpost():
    data = request.get_json(force=True)
    data = json.loads(data)
    new_acc = account.Account(data)
    session.add(new_acc)
    session.commit()
    return {'Code': 200}
    
@app.route('/users/update', methods=['PUT'])
def update_account():
    data = request.get_json(force=True)
    data = json.loads(data)
    id = data['id']
    stmt = select(account.Account).where(
        account.Account.id.in_([id])
    )
    for obj in session.scalars(stmt):
        feature = obj

    for key in data:
        setattr(feature, key, data[key])
        
    session.commit()
    return feature.as_dict(), 200
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
