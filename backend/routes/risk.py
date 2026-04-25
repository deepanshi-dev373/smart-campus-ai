from flask import Blueprint, request
from ai.risk_model import predict

risk_routes = Blueprint('risk', __name__)

@risk_routes.route('/risk', methods=['POST'])
def risk():
    att = int(request.json['attendance'])
    return {"risk": predict(att)}