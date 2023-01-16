from flask import Blueprint

from .views import CustomerAPI
from .views import CustomerListAPI

customer_bp = Blueprint('customers', __name__)

customer_view = CustomerAPI.as_view("customer")
customer_list_view = CustomerListAPI.as_view("customers")

customer_bp.add_url_rule("", view_func=customer_list_view, methods=["GET", "POST"])
customer_bp.add_url_rule("/<path:id>", view_func=customer_view, methods=["GET"])
