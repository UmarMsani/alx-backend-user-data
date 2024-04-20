#!/usr/bin/env python3
""" Model representing a user session.
"""
import hashlib
from models.base import Base


class UserSession(Base):
    """ Class representing a user.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialization method. """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
