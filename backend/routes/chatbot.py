from flask import Blueprint, request

chatbot_routes = Blueprint('chatbot', __name__)

@chatbot_routes.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get("message", "")
    return {"reply": "AI Bot: Hello 👋"}