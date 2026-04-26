from flask import Blueprint, render_template

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/admin/dashboard')
def dashboard():
    return render_template("admin.html")

@admin_routes.route('/admin/students')
def students():
    return {"data": "Students list"}

@admin_routes.route('/admin/faculty')
def faculty():
    return {"data": "Faculty list"}

@admin_routes.route('/admin/analytics')
def analytics():
    return {"data": "Analytics dashboard"}