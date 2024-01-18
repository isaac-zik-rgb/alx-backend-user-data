#!/usr/bin/env python3
"""add session auth"""
from api.v1.views.session_auth import *


app_views.route("/auth_session/logout", methods=['DELETE'], strict_slashes=False)(session_login)