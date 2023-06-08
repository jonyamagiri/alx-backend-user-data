#!/usr/bin/env python3
"""  module for authentication """

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the input password using bcrypt"""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password
