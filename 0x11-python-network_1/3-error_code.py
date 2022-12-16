#!/usr/bin/python3
"""script that takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
from urllib import request, error
import sys


if __name__ == "__main.__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
