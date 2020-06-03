#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tru Jun 3 15:13:37 2020

@author: Robinson Montes
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    new_list = load_from_json_file('add_item.json')
except:
    new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

try:
    save_to_json_file(new_list, 'add_item.json')
except:
    pass
