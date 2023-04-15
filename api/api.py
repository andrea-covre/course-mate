from flask import Flask, request, jsonify
from flask_restful import Api
from sqlalchemy import select

from api.utils import load_request_data
from api.planetscale_connection import get_db_session
from api.queries import Database
from api.models import account, major, section, section_instructor, instructor, class_, location, semester

session = get_db_session(autocommit=True)
app = Flask(__name__)
api = Api(app)
db = Database(session)

# GET /users?id=<user_id>
@app.route('/users', methods=['GET'])
def users():
    args = request.args
    id = args.get('id')
    user = db.get_account_by_id(id)
    if user:
        return user.as_dict(), 200
    else:
        return {}, 404
    
# POST /users/add
@app.route('/users/add', methods=['POST'])
def add_user():
    data = request.get_json(force=True)
    data = load_request_data(data)
    new_account_id = db.add_account(data)
    return {'Code': 200, 'id': new_account_id}

# DELETE /users/delete?id=<user_id>
@app.route('/users/delete', methods=['DELETE'])
def delete_user():
    args = request.args
    id = args.get('id')
    user_to_delete = db.get_account_by_id(id)
    
    if user_to_delete is not None:
        db.delete_account(user_to_delete)
        return {'Code': 200, 'Message': f'User with ID {id} deleted successfully.'}
    else:
        return {'Code': 404, 'Message': f'User with ID {id} not found.'}
    
# GET /majors
@app.route('/majors', methods=['GET'])
def get_majors():
    majors = db.get_majors()
    return {'Code': 200, "majors": majors}
    
@app.route('/users/update', methods=['PUT'])
def update_account():
    data = request.get_json(force=True)
    data = load_request_data(data)
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

#TO BE TESTED
#Example = /users/schedule?id=<user_id>
@app.route('/users/schedule', methods=['GET'])
def update_account_schedule():
    data = request.get_json(force=True)
    data = load_request_data(data)
    id = data['account_id']
    stmt = select(schedule.Schedule).where(
        schedule.Schedule.account_id.in_([id])
    )
    schedule_objects = []
    for obj in session.scalars(stmt):
        schedule_objects.append(obj)

    sections = []
    for schedule_object in schedule_objects:
        section_id = schedule_object.section_id
        stmt = select(section.Section).where(
            section.Section.id.in_([section_id])
        )
        curr_section = session.scalar(stmt)
        sections.append(curr_section)

    schedule = []
    for curr_section in sections:
        curr_schedule = {}
        semester_id = curr_section.semester_id
        curr_semester = session.scalar(select(semester.Semester).where(
            semester.Semester.id.in_([semester_id])
        ))
        curr_schedule['semester'] = curr_semester.as_dict()

        class_id = curr_section.class_id
        curr_class = session.scalar(select(class_.Class).where(
            class_.Class.id.in_([class_id])
        ))
        curr_schedule['class'] = curr_class.as_dict()
        curr_schedule['crn'] = curr_section.crn
        curr_schedule['section_name'] = curr_section.section_name
        instructor_id = curr_section.instructor_id
        curr_instructor = session.scalar(select(instructor.Instructor).where(
            instructor.Instructor.id.in_([instructor_id])
        ))
        curr_schedule['instructor'] = curr_instructor.as_dict()
        curr_schedule['times'] = curr_section.times

        location_id = curr_section.location_id
        curr_location = session.scalar(select(location.Location).where(
            location.Location.id.in_([location_id])
        ))
        curr_schedule['semester'] = curr_location.as_dict()
        schedule.append(curr_schedule)

    return schedule, 200
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)

