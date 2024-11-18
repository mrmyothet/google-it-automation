#!/usr/bin/env python3


def validate_user(username, min_length):
    assert type(username) == str, "username must be a string"

    if min_length < 1:
        raise ValueError("min_length must be at least 1")

    if len(username) < min_length:
        return False

    if not username.isalnum():
        return False

    return True
