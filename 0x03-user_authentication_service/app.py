#!/usr/bin/env python3
"""
A basic Flask app
"""

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/")
def index():
    """Root endpoint returning a welcome message in JSON format."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
