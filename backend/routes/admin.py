from flask import Blueprint, render_template

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin.html")