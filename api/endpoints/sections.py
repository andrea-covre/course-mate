from flask import Blueprint, request

from api.resources import db

ROUTE_PREFIX = '/sections'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)


# GET /sections/?semester_id=<semester_id>
@blueprint.route('/', methods=['GET'])
def get_majors():
    args = request.args
    semester_id = args.get('semester_id')
    sections = db.get_sections(semester_id)
    
    return sections, 200
