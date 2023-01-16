from flask import Blueprint

from .views import UserAPI
from .views import UserListAPI

user_bp = Blueprint('users', __name__)

user_view = UserAPI.as_view("user")
user_list_view = UserListAPI.as_view("users")

user_bp.add_url_rule("", view_func=user_list_view, methods=["GET", "POST"])
user_bp.add_url_rule("", view_func=user_view, methods=["GET"])
