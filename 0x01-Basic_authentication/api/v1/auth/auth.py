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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path += '/'
        if path[-1] == '*' and path[:-1] not in excluded_paths:
            return True
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

        return False

    def authorization_header(self, request=None) -> str:
        """ an authorization header method that returns the request object
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """This function returns the current user that is authorized
        """
        return None