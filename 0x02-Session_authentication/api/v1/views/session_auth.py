#!/usr/bin/env python3
"""A Session Authentication routes"""
from flask import jsonify
from api.v1.views import app_views

from os import getenv
from flask import request
from models.user import User

@app_views.route("/auth_session/login", methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """Handle login route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this emil"}), 404
    for user in users:
        from api.v1.app import auth
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
