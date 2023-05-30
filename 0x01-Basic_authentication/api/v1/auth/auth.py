#!/usr/bin/env python3
""" module auth.py to manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path.

        Args:
            path (str): The path being accessed.
            excluded_paths (List[str]): List of paths that are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request.

        Args:
            request (Request, optional): The Flask request object. Defaults to None.

        Returns:
            str: The authorization header value.
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user.

        Args:
            request (Request, optional): The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current authenticated user.
        """
        return None
