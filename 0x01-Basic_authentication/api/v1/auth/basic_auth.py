#!/usr/bin/env python3
""" module basic_auth.py to implement Basic authentication"""

import base64
import binascii
from typing import Tuple, TypeVar, Optional
from api.v1.auth.auth import Auth
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a Base64 Authorization header"""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_value = decoded_bytes.decode('utf-8')
            return decoded_value
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extract user credentials from the decoded Base64 header."""
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        credentials = decoded_base64_authorization_header.rsplit(':', 1)
        if len(credentials) != 2:
            return None, None

        user_email, user_password = credentials
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str, user_pwd: str,
                                     ) -> TypeVar('User'):
        """Retrieve a User instance based on email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # get list of User objects matching the email
        attr = {'email': user_email}
        user_init = User()
        user_list = User.search(attr)

        user = None
        for usr in user_list:
            if usr.is_valid_password(user_pwd):
                user = usr
                break

        return user

    def current_user(self, request=None) -> User:
        """Retrieve the User instance for a request."""
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_header)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
