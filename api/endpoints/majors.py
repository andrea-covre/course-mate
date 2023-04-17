from flask import Blueprint, request

from api.resources import db

ROUTE_PREFIX = '/majors'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)


# GET /majors
@blueprint.route('', methods=['GET'])
def get_majors():
    majors = db.get_majors()
    return {'Code': 200, "majors": majors}
