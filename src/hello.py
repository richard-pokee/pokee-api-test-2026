#!/usr/bin/env python3
"""A simple hello world module for API testing."""


def hello(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
