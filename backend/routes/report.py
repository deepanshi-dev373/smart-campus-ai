from flask import Blueprint

report_routes = Blueprint('report', __name__)

@report_routes.route('/report')
def report():
    return "Report Generated ✅"