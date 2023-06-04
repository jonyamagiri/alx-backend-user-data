#!/usr/bin/env python3
""" module auth.py to manage the API authentication"""

from flask import request
from typing import List, TypeVar
import fnmatch
from os import getenv


class Auth:
    """Basic uthentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user."""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request."""
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
