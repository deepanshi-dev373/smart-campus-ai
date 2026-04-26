from flask import Flask
from routes.auth import auth_routes
from routes.dashboard import dashboard_routes
from routes.ai import ai_routes

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(auth_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(ai_routes)

if __name__ == "__main__":
    app.run(debug=True)