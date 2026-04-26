from flask import Blueprint

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/admin/dashboard')
def admin_dash():
    return {"msg": "Admin Dashboard"}

@admin_routes.route('/students')
def students():
    return {"data": "student list"}

@admin_routes.route('/faculty')
def faculty():
    return {"data": "faculty list"}