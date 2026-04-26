from flask import Flask, render_template
from routes.auth import auth_routes

app = Flask(__name__)

# Register blueprint
app.register_blueprint(auth_routes)

# Landing page
@app.route('/')
def home():
    return render_template("landing.html")

if __name__ == '__main__':
    app.run(debug=True)