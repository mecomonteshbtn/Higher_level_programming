#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 05:14:59 2020

@author: meco
"""
from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as response:
        bytes_content = response.read()
        content = bytes_content.decode('utf-8')
        string = """Body response:
            \t- type: {}
            \t- content: {}
            \t- utf8 content: {}""".format(type(bytes_content), bytes_content,
                                            content)
        print(string)
