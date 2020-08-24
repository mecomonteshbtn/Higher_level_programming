#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:02:53 2020

@author: Robinson Montes
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    username = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
    response = get(url)
    try:
        obj = response.json()
        for i in range(10):
            print('{}: {}'.format(obj[i].get('sha'),
                                  obj[i].get('commit').get('author')
                                  .get('name')))
    except ValueError:
        pass
