#!/usr/bin/env python3
""" Main 101
"""
from api.v1.auth.auth import Auth

# Instantiate Auth
auth = Auth()

# Test the require_auth method
excluded_paths = ["/api/v1/stat*"]

# Test paths
paths = ["/api/v1/users", "/api/v1/status", "/api/v1/stats"]

for path in paths:
    auth_required = auth.require_auth(path, excluded_paths)
    print(f"Path: {path}, Auth Required: {auth_required}")
