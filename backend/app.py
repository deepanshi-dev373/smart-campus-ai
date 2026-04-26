from flask import Flask, render_template
from routes.auth import auth_routes
from routes.student import student_routes
from routes.teacher import teacher_routes
from routes.admin import admin_routes
from routes.chatbot import chatbot_routes
from routes.risk import risk_routes
import os

app = Flask(__name__)

app.register_blueprint(auth_routes)
app.register_blueprint(student_routes)
app.register_blueprint(teacher_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(chatbot_routes)
app.register_blueprint(risk_routes)

@app.route('/')
def home():
    return render_template("landing.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))