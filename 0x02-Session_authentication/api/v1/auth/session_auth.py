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

    def user_id_for_session_id(self, session_id: str = None) -> Optional[str]:
        """Returns a User ID based on a Session ID."""
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value."""
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None

        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session / logout."""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
