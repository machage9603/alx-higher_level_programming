#!/usr/bin/python3
""
send  a POST request to the passed URL with the email as a parameter

Usage: ./2-post_email.py <URL> <email>
    - URL: the URL to send the request to
    - email: the email to send in the POST

    - displays the body of the response
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    """Ensures that the code is not executed when imported"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data=data)
    with urlopen(req) as response:
        body = response.read()
    print(body.decode("utf-8"))
