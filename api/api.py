import argparse

from flask import Flask
from flask_restful import Api
 
from api.endpoints.users import blueprint as users_blueprint
from api.endpoints.majors import blueprint as majors_blueprint
from api.endpoints.schedule import blueprint as schedule_blueprint
from api.endpoints.friendship import blueprint as friendship_blueprint


app = Flask(__name__)
api = Api(app)

app.register_blueprint(users_blueprint)
app.register_blueprint(majors_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(friendship_blueprint)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask app locally or publicly')
    parser.add_argument('-p', '--public', action='store_true', help='run the app publicly')
    args = parser.parse_args()
    
    if args.public:
        app.run(host='0.0.0.0', port=8080)
        
    else:
        app.run(debug=True, port=5000)
