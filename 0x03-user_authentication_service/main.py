#!/usr/bin/env python3
"""Module for simple end-to-end (E2E) integration tests for `app.py`.
"""

import requests

BASE_URL = "http://0.0.0.0:5000"

def register_user(email: str, password: str) -> None:
    response = requests.post(f"{BASE_URL}/register", json={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json()["message"] == "User successfully registered."

def log_in_wrong_password(email: str, password: str) -> None:
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid email or password."

def log_in(email: str, password: str) -> str:
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
    assert response.status_code == 200
    return response.json()["session_id"]

def profile_unlogged() -> None:
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 401
    assert response.json()["message"] == "Unauthorized access."

def profile_logged(session_id: str) -> None:
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == EMAIL

def log_out(session_id: str) -> None:
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.post(f"{BASE_URL}/logout", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Logged out successfully."

def reset_password_token(email: str) -> str:
    response = requests.post(f"{BASE_URL}/reset-password", json={"email": email})
    assert response.status_code == 200
    return response.json()["reset_token"]

def update_password(email: str, reset_token: str, new_password: str) -> None:
    data = {"email": email, "reset_token": reset_token, "new_password": new_password}
    response = requests.post(f"{BASE_URL}/update-password", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Password updated successfully."


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


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
