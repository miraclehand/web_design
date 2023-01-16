from flask.views import MethodView
from flask import jsonify
from flask import request

from app import db
from .models import Customer

class CustomerAPI(MethodView):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        return {"id": customer.id, "name": customer.customer_name}

class CustomerListAPI(MethodView):
    def get(self):
        return [{"id": customer.id, "name": customer.customer_name} for customer in Customer.query.all()]

    def post(self):
        id = request.json.get("id")
        customer_name = request.json.get("customer_name")
        db.session.add(Customer(id, customer_name))
        db.session.commit()
        return {}, 201
