#!/usr/bin/env python3

"""
hash passwords using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashed password.

    Args:
        password (str): A string containing the plain text
        password to be hashed.

    Returns:
        returns a bytestring of the hashed pwd
    Exceptions:
        Raises TypeError if the pwd is not of type str
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(stored_pwd: bytes, input_pwd: str) -> bool:
    """
    Validates whether the provided password matches hashed password
    Args:
        input_pwd (str): the entered password
        stored_pwd (str): password stored in the db
    Returns:
        return a bool
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
