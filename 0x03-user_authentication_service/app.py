#!/usr/bin/env python3
""" module that sets up a basic Flask app """

from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ Returns the given JSON payload """
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Creates a new user with the provided email and password """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Logs in a user and creates a session."""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs out a user."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    response = redirect('/')
    response.delete_cookie('session_id')
    return response


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Retrieves the user profile based on the session ID."""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    response_data = {'email': user.email}
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
