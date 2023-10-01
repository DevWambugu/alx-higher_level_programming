#!/usr/bin/python3
'''
Please list 10 commits (from the most recent to oldest)
script takes 2 arguments in order to solve this challenge
'''
import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo_name = sys.argv[1]
    url = ('https://api.github.com/repos/{}/{}/commits'
           .format(repo_name, owner))

    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[0:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
