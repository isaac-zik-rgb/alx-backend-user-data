#!/usr/bin/env python3
"""
Basic Authentication class that authenticate a user
"""

from flask import request


class Auth:
    """A Basic Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for a given path.
        This function determines whether authentication is
        required for a specific
        path, taking into account a list of excluded paths
        where authentication is not enforced.
        Parameters:
             - path (str): The path for which authentication
             requirement is being checked.
             - excluded_paths (List[str]): A list of paths where
             authentication is not enforced.
             Returns:
             bool: True if authentication is required for the
             given path, False otherwise.
        Example:
             ```
             auth_required = require_auth('/secured/resource',
             excluded_paths=['/public', '/unsecured'])
             if auth_required:
             # Perform authentication logic
             else:
             # Authentication is not required for the given path
             ```
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
