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
    rep_name = sys.argv[1]
    rep_owner = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(rep_name, rep_user))
    response_json = response.json()

    if response.status_code != 200:
        print("None")
    else:
        for key, value in response_json:
            print("{}: {}".format(response_json['sha'], respos))
