#!/usr/bin/python3
'''
Python script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter
'''
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": q}

    try:
        response = requests.get(url, data=data)
        response_json = response.json()

        if response_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
