#!/usr/bin/env python3
""" The Module of Authentication
"""
from flask import request
from os import getenv
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path
            Args:
            - path (str): URL path to be checked
            - excluded_paths (List of str): List of paths that do not
            require authentication
        Returns:
            - True if the path is not in excluded_paths, otherwise False
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header from a request object """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns User instance from information from request object"""
        return None

    def session_cookie(self, request=None):
        """
        Retrieve the session cookie value from the request.
        Args:
            request: The request object containing the session cookie.
        Returns:
            The session cookie value.
        """

        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id
