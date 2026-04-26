from flask import Blueprint, request

risk_routes = Blueprint('risk', __name__)

@risk_routes.route('/risk', methods=['GET','POST'])
def risk():
    return {"risk": "Low Risk ✅"}