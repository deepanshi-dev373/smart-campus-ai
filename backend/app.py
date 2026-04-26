from flask import Flask, render_template
from routes.student import student_routes
from routes.teacher import teacher_routes
from routes.admin import admin_routes
from routes.ai import ai_routes

app = Flask(__name__)

app.register_blueprint(student_routes)
app.register_blueprint(teacher_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(ai_routes)

@app.route('/')
def home():
    return render_template("landing.html")

if __name__ == "__main__":
    app.run(debug=True)