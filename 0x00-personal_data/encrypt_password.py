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
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(stored_pwd: bytes, input_pwd: str) -> bool:
    """
    Validates whether the provided password matches hashed password
    Args:
        input_pwd (str): the entered password
        stored_pwd (str): password stored in the db
    Returns:
        return a bool
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
