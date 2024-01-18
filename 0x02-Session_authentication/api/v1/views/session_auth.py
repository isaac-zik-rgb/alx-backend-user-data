#!/usr/bin/env python3
"""A Session Authentication routes"""
from flask import jsonify
from api.v1.app import app_views
from models.user import User
from os import getenv

@app_views.route("/auth_session/login", methods=['POST'], strict_slashes=False)
def session_login(email: str, password: str) -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the status of the API
    """
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    
    user = User.search({"email": email})
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)
    return response


    