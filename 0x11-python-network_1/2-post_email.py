#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:02:53 2020

@author: Robinson Montes
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    email = urlencode(email)
    email = email.encode('ascii')
    request = Request(url, email)
    with urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
