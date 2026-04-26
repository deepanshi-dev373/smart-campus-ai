from flask import Blueprint, request

risk_routes = Blueprint('risk', __name__)

@risk_routes.route('/risk', methods=['POST'])
def risk():
    att = int(request.json.get("attendance", 0))

    if att < 50:
        return {"risk": "High Risk ❌"}
    elif att < 75:
        return {"risk": "Medium Risk ⚠️"}
    return {"risk": "Low Risk ✅"}