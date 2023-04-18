from flask import Blueprint, request

from api.resources import db

ROUTE_PREFIX = '/semester'

blueprint = Blueprint(ROUTE_PREFIX, __name__, url_prefix=ROUTE_PREFIX)


# GET /semester
@blueprint.route('', methods=['GET'])
def get_semesters():
    semesters = db.get_semesters()
    return semesters, 200
