import sys
import argparse

from flask_restful import Api
from flask import Flask, request, jsonify

from api.resources import db
 
from api.auth import authenticate
from api.endpoints.users import blueprint as users_blueprint
from api.endpoints.majors import blueprint as majors_blueprint
from api.endpoints.schedule import blueprint as schedule_blueprint
from api.endpoints.semester import blueprint as semester_blueprint
from api.endpoints.friendship import blueprint as friendship_blueprint


app = Flask(__name__)
api = Api(app)


app.register_blueprint(users_blueprint)
app.register_blueprint(majors_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(friendship_blueprint)
app.register_blueprint(semester_blueprint)


@app.before_request
def require_auth_token():
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify({'message': 'Authorization token is missing'}), 401
    
    if not authenticate(auth_token):
        return jsonify({'message': 'Authorization token is invalid'}), 401
    
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'An internal server error occurred.'}), 500

def main():
    parser = argparse.ArgumentParser(description='Run Flask app locally or publicly')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--public', action='store_true', help='run the app publicly')
    group.add_argument('-e', '--endpoints', action='store_true', help='print out all the app\'s endpoints')

    args = parser.parse_args()
    
    if args.endpoints:
        print('Endpoints:')
        for rule in app.url_map.iter_rules():
            methods = str(",".join(rule.methods))
            print("  {:<30} {}".format(str(rule), methods))
        sys.exit(0)

    if args.public:
        app.run(host='0.0.0.0', port=8080)
        
    else:
        app.run(debug=True, port=5000)
    

if __name__ == '__main__':
    main()
