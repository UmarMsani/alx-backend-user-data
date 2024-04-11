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
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(stored_pwd: bytes, input_pwd: str) -> bool:
    """
    Validates whether the provided password matches hashed password
    Args:
        input_pwd (str): the entered password
        stored_pwd (str): password stored in the db
    Returns:
        return a bool
    """
    return bcrypt.checkpw(input_pwd.encode(), stored_pwd)
