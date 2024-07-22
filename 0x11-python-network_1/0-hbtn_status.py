#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import urllib.requests


url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
