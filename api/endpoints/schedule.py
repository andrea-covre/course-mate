from flask import Blueprint, request, jsonify

from api.resources import db
from api.utils import load_request_data

ROUTE_PREFIX = '/schedule'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)

    
# POST /add
@blueprint.route('/add', methods=['POST'])
def add_section():
    data = request.get_json(force=True)
    data = load_request_data(data)
    
    user_id = data.get('user_id')
    semester_id = data.get('semester_id')
    crn = data.get('crn')
    subject_code = data.get('subject_code')
    class_number = data.get('class_number')
    section_code = data.get('section_code')
    
    if user_id is None:
        return {'Message': f'User ID not provided'}, 400
    
    if semester_id is None:
        return {'Message': f'Semester ID not provided'}, 400
    
    crn_provided = crn is not None
    section_provided = (
        subject_code is not None and 
        class_number is not None and 
        section_code is not None)
    
    if crn_provided and section_provided:
        return {'Message': f'Both CRN and section info provided, provide only one'}, 400
    
    if not crn_provided and not section_provided:
        return {'Message': f'CRN or section info not provided'}, 400
    
    if crn_provided:
        section_id = db.get_section_id_by_crn(semester_id, crn)
        
    if section_provided:
        class_id = db.get_class_id(subject_code, class_number)
        if not class_id:
            section_id = None
        else:        
            section_id = db.get_section_id_by_class_id(semester_id, class_id, section_code)
        
    if section_id is None:
        return {'Message': f'Could not find the section specified'}, 404
        
    db.add_schedule_entry(user_id, section_id)
    
    return {}, 200


# GET ?id=<user_id>&semester=<semester_id>
@blueprint.route('/', methods=['GET'])
def get_schedule():
    args = request.args
    user_id = args.get('id')
    semester_id = args.get('semester')
    
    schedule = db.get_user_schedule(user_id, semester_id)
    if schedule:
        return schedule, 200
    else:
        return {}, 404
    
    
# GET /common?id_1=<user_id_1>&id_2=<user_id_2>&semester=<semester_id>
@blueprint.route('/common', methods=['GET'])
def get_common_schedule():
    args = request.args
    user_1_id = args.get('id_1')
    user_2_id = args.get('id_2')
    semester_id = args.get('semester')
    
    schedule = db.get_common_schedule(user_1_id, user_2_id, semester_id)
    if schedule:
        return schedule, 200
    else:
        return {}, 404
    
