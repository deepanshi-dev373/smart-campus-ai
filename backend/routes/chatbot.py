from flask import Blueprint, request

chatbot_routes = Blueprint('chatbot', __name__)

@chatbot_routes.route('/chat', methods=['GET','POST'])
def chat():
    return {"reply": "Hello from AI 🤖"}