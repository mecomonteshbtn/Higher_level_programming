#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:02:53 2020

@author: Robinson Montes
"""
from requests import post, get
from sys import argv
from base64 import b64encode


if __name__ == '__main__':
    APIkey = '{}:{}'.format(argv[1], argv[2])
    base64_encode = b64encode(APIkey.encode()).decode('utf-8')
    data = {'grant_type': 'client_credentials'}
    header = {'Authorization': 'Basic {}'.format(base64_encode),
              'Content-Type':
              'application/x-www-form-urlencoded;charset=UTF-8'}
    req = post('https://api.twitter.com/oauth2/token', headers=header,
               data=data)
    response = req.json()
    token = response.get('access_token')
    header = {'Authorization': 'Bearer {}'.format(token)}
    data = {'q': argv[3], 'count': 5}
    req = get('https://api.twitter.com/1.1/search/tweets.json',
              headers=header, params=data)
    response = req.json()
    tweets = response.get('statuses')
    for tweet in tweets:
        print('[{}] {} by {}'.format(tweet.get('id'), tweet.get('text'),
                                     tweet.get('user').get('name')))
