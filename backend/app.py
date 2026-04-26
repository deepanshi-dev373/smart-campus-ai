from flask import Flask, render_template
from routes.auth import auth_routes
from routes.dashboard import dashboard_routes
from routes.ai import ai_routes

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(auth_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(ai_routes)

@app.route('/')
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)