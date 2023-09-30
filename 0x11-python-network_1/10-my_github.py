#!/usr/bin/python3
'''
Python script that takes your
GitHub credentials
(username and password)
and uses the GitHub API to display your id
'''
import requests
import sys

if __name__ == "__main__":
    token = sys.argv[2]
    username = sys.argv[1]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    response_json = response.json()

    if response.status_code != 200:
        print("None")
    else:
        print("{}".format(response_json['id']))
