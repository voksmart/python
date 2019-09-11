# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:44:26 2019

@author: Mohit
"""
"""
Objective :  Find the list of all reserved keywords in Python 
"""

# import keyword module which contains keyword list and  
# handles keyword related operations
import keyword 

# Empty list to store Python Keywords
keywordList=[]

for keywd in keyword.kwlist:
    keywordList.append(keywd)  

print('Python Keywords are :\n')
print(keywordList)
