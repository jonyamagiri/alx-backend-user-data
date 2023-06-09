#!/usr/bin/env python3
""" End-to-end integration tests for the user_authentication_service module """

import requests

BASE_URL = "http://localhost:5000"
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Testing user registration"""
    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}
    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.json() == {"message": "email already registered"}
    print("User registered successfully.")


def log_in_wrong_password(email: str, password: str) -> None:
    """Testing user login with wrong password"""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 401
    print("Failed to log in with wrong password as expected.")


def log_in(email: str, password: str) -> str:
    """Testing user login as expected"""
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print("Logged in successfully.")
    session_id = response.cookies.get("session_id")
    return session_id


def profile_unlogged() -> None:
    """Test for accessing profile while unlogged."""
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403
    print("Access to profile unlogged as expected.")


def profile_logged(session_id: str) -> None:
    """Tests retrieval of the profile data of a logged-in user."""
    url = f"{BASE_URL}/profile"
    header = {'session_id': session_id}
    response = requests.get(url, cookies=header)
    assert response.status_code == 200
    profile_data = response.json()
    assert "email" in profile_data
    print("Profile data:", profile_data)


def log_out(session_id: str) -> None:
    """Test log out of user session"""
    url = f"{BASE_URL}/sessions"
    data = {"session_id": session_id}
    response = requests.delete(url, cookies=data)
    assert response.status_code == 200
    print("Logged out successfully.")


def reset_password_token(email: str) -> str:
    """Tests password reset request"""
    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print("Password reset_token successful.")
    reset_token = response.json().get("reset_token")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests password update request"""
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(url, data=data)
    assert response.status_code == 200
    print("Password updated successfully.")


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
