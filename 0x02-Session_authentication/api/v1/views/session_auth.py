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
    for user in user:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            json = jsonify(user.to_json())
            json.set_cookie(getenv('SESSION_NAME'), session_id)
            return json
        return jsonify({"error": "wrong password"}), 40