from flask import Flask, render_template, session
from routes.auth import auth_routes
from routes.attendance import attendance_routes
from routes.chatbot import chatbot_routes
from routes.risk import risk_routes
from routes.report import report_routes

import os

app = Flask(__name__)
app.secret_key = "secret123"

# Register all routes
app.register_blueprint(auth_routes)
app.register_blueprint(attendance_routes)
app.register_blueprint(chatbot_routes)
app.register_blueprint(risk_routes)
app.register_blueprint(report_routes)

# Home
@app.route('/')
def home():
    return render_template("login.html")

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("dashboard.html")
    return "Login First ❌"

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))