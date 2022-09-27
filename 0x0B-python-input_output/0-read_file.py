#!/usr/bin/python3
"""Defines a text file reading functiom"""


def read_file(filename=""):
    """Print the content of UTF-8 text"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
