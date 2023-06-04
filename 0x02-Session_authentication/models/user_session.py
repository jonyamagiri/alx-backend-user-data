#!/usr/bin/env python3
""" module for managing session IDs """

from models.base import Base


class UserSession(Base):
    """ User session class for managing session IDs """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize the session instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
