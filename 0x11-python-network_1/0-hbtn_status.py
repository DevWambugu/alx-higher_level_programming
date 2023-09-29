#!/usr/bin/python3
'''
a Python script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html_response = response.read().decode('utf-8')
    content = response.read()
    print("Body response:")
    print('\t- type: {_type}'.format(_type=type(content)))
    print('\t- content: {_content}'.format(_content=content))
    print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=html_response))
