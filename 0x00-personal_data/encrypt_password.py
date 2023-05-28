#!/usr/bin/env python3
""" module encrypt_password.py """

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt."""
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if the provided password matches the hashed password."""
    encoded_password = password.encode('utf-8')
    return bcrypt.checkpw(encoded_password, hashed_password)
