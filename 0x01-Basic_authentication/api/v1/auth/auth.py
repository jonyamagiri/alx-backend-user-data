""" module auth.py to manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path.
        Args:
            path (str): The path being accessed.
            excluded_paths (List[str]): List of paths that are excluded from authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request.
        Args:
            request (Request, optional): The Flask request object. Defaults to None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user.
        Args:
            request (Request, optional): The Flask request object. Defaults to None.
        """
        return None
