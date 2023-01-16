from flask.views import MethodView
from flask import jsonify
from flask import request

from app import db
from .models import User

class UserAPI(MethodView):
    def get(self, id):
        user = User.query.get_or_404(id)
        return {"id": user.id, "username": user.username, "password_hash": user.password_hash}

class UserListAPI(MethodView):
    def get(self):
        return [{"id": user.id, "name": user.username, "password_hash": user.password_hash} for user in User.query.all()]

    def post(self):
        id = request.json.get("id")
        user_name = request.json.get("user_name")
        db.session.add(User(id, user_name))
        db.session.commit()
        return {}, 201
