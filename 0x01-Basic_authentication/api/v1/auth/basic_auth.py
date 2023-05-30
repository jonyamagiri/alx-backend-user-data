#!/usr/bin/env python3
""" module basic_auth.py to implement Basic authentication"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ basic authentication class """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the Base64 part of the Authorization header"""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
