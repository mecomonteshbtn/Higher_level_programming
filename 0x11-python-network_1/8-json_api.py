#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:02:53 2020

@author: Robinson Montes
"""
from requests import post, codes
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = {'q': argv[1]}
    else:
        q = {'q': ''}
    response = post(url, data=q)
    if response.status_code == codes.ok:
        obj = response.json()
        if len(obj) == 0:
            print('No result')
            exit()
        print('[{}] {}'.format(obj['id'], obj['name']))
    else:
        print('No result')
        exit()
