#!/usr/bin/env python3
""" module for session authentication """

from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import Optional


class SessionAuth(Auth):
    """ class for session authentication implementation """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """Creates a session ID for a user_id."""
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
