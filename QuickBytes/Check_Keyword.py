# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:06:18 2019

@author: Mohit
"""
"""
Objective :
   Find if a string or list element is a Python reserved keyword or not
"""
# lets import "keyword" module which contains "keyword" list and handles 
# operations related to keywords
import keyword

keywordlist=["hello","for","guest","sky","while","list"]

for checkstr in keywordlist:
    if keyword.iskeyword(checkstr):
        print(checkstr + " : is a Python reserved keyword.")
    else:
        print(checkstr + " : is a not a Python reserved keyword.")
    












