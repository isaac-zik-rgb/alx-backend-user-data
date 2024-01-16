#!/usr/bin/env python3
"""
Basic Authentication class that authenticate a user
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """A Basic Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for a given path.
        This function determines whether authentication is
        required for a specific path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ an authorization header method that returns the request object
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """This function returns the current user that is authorized
        """
        return request
