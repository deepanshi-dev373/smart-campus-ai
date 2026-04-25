from flask import Blueprint, request
from ai.chatbot_ai import chatbot_reply

chatbot_routes = Blueprint('chatbot', __name__)

@chatbot_routes.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message']
    return {"reply": chatbot_reply(msg)}