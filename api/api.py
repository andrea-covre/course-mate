from flask import Flask, request, jsonify
from flask_restful import Api
from sqlalchemy import select

from api.utils import load_request_data
from api.planetscale_connection import get_db_session
from api.models import account, major, section, section_instructor, instructor, class_, location, semester

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
    print(type(data))
    data = load_request_data(data)
    new_acc = account.Account(data)
    session.add(new_acc)
    session.commit()
    return {'Code': 200}
    
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

