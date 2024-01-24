#!/usr/bin/env python3
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
