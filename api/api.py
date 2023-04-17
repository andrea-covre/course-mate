import argparse

from flask import Flask
from flask_restful import Api
 
from api.endpoints.users import blueprint as users_blueprint
from api.endpoints.majors import blueprint as majors_blueprint
from api.endpoints.schedule import blueprint as schedule_blueprint


app = Flask(__name__)
api = Api(app)

app.register_blueprint(users_blueprint)
app.register_blueprint(majors_blueprint)
app.register_blueprint(schedule_blueprint)

# #Example = /users/schedule?id=<user_id>
# @app.route('/users/schedule', methods=['GET'])
# def update_account_schedule():
#     data = request.get_json(force=True)
#     data = load_request_data(data)
#     id = data['account_id']
#     stmt = select(schedule.Schedule).where(
#         schedule.Schedule.account_id.in_([id])
#     )
#     schedule_objects = []
#     for obj in session.scalars(stmt):
#         schedule_objects.append(obj)

#     sections = []
#     for schedule_object in schedule_objects:
#         section_id = schedule_object.section_id
#         stmt = select(section.Section).where(
#             section.Section.id.in_([section_id])
#         )
#         curr_section = session.scalar(stmt)
#         sections.append(curr_section)

#     schedule = []
#     for curr_section in sections:
#         curr_schedule = {}
#         semester_id = curr_section.semester_id
#         curr_semester = session.scalar(select(semester.Semester).where(
#             semester.Semester.id.in_([semester_id])
#         ))
#         curr_schedule['semester'] = curr_semester.as_dict()

#         class_id = curr_section.class_id
#         curr_class = session.scalar(select(class_.Class).where(
#             class_.Class.id.in_([class_id])
#         ))
#         curr_schedule['class'] = curr_class.as_dict()
#         curr_schedule['crn'] = curr_section.crn
#         curr_schedule['section_name'] = curr_section.section_name
#         instructor_id = curr_section.instructor_id
#         curr_instructor = session.scalar(select(instructor.Instructor).where(
#             instructor.Instructor.id.in_([instructor_id])
#         ))
#         curr_schedule['instructor'] = curr_instructor.as_dict()
#         curr_schedule['times'] = curr_section.times

#         location_id = curr_section.location_id
#         curr_location = session.scalar(select(location.Location).where(
#             location.Location.id.in_([location_id])
#         ))
#         curr_schedule['semester'] = curr_location.as_dict()
#         schedule.append(curr_schedule)

#     return schedule, 200

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask app locally or publicly')
    parser.add_argument('-p', '--public', action='store_true', help='run the app publicly')
    args = parser.parse_args()
    
    if args.public:
        app.run(host='0.0.0.0', port=8080)
        
    else:
        app.run(debug=True, port=5000)
