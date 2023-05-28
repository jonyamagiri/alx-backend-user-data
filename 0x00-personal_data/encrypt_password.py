#!/usr/bin/env python3
""" module encrypt_password.py """

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt."""
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password
