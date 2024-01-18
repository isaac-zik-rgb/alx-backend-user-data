#!/usr/bin/env python3
"""A Session Authentication routes"""
from flask import jsonify
from api.v1.views import app_views
from models.user import User
from os import getenv
from flask import request

@app_views.route("/auth_session/login", methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """Handle login route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if User.is_valid_password(user[0].password, password) is False:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response