#!/usr/bin/env python3
""" module auth.py to manage the API authentication"""

from flask import request
from typing import List, TypeVar


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
            if path.startswith(excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user."""
        return None
