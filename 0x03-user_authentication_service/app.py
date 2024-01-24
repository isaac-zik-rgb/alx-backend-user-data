#!/usr/bin/env python
"""Basic Flask App"""

from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Return json response
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})
