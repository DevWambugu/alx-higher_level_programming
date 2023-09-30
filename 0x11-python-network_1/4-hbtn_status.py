#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print('\t- type: {_type}'.format(_type=type(content)))
    print('\t- content: {_content}'.format(_content=content))
