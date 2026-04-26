from flask import Blueprint, request

ai_routes = Blueprint('ai', __name__)

@ai_routes.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message']

    if "attendance" in msg:
        reply = "Your attendance is good 👍"
    else:
        reply = "I am AI Assistant 🤖"

    return {"reply": reply}

@ai_routes.route('/risk', methods=['POST'])
def risk():
    att = int(request.json['attendance'])

    if att < 50:
        return {"risk": "High Risk ❌"}
    elif att < 75:
        return {"risk": "Medium Risk ⚠️"}
    return {"risk": "Low Risk ✅"}