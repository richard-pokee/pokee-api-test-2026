"""Tests for hello module."""
from hello import hello


def test_hello_default():
    assert hello() == "Hello, World!"


def test_hello_name():
    assert hello("Pokee") == "Hello, Pokee!"
