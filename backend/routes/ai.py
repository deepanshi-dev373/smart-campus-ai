from flask import Blueprint, request

ai_routes = Blueprint('ai', __name__)

# Chatbot
@ai_routes.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get("message")
    return {"reply": f"AI: You said '{msg}'"}

# Risk predictor
@ai_routes.route('/risk', methods=['POST'])
def risk():
    att = int(request.json.get("attendance"))

    if att < 50:
        return {"risk": "High Risk ❌"}
    elif att < 75:
        return {"risk": "Medium Risk ⚠️"}
    return {"risk": "Low Risk ✅"}

# Smart notice generator
@ai_routes.route('/generate_notice', methods=['POST'])
def notice():
    topic = request.json.get("topic")
    return {"notice": f"Important Notice: {topic} will be conducted soon. All students must attend."}