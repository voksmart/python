# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:32:20 2019

@author: Mohit
"""
"""
Objective : A few basic ways to use range function
"""
"""

range(start,stop,step)

- Range returns a sequence of numbers 
  with the specified criteria
- starting point of the sequence 
  (default = 0)
- end point of the sequence 
  (not included in output)
- step value determines increment/
  decrement steps 
  between in iteration
- works with integer values only
- step value can be positive or 
  negative (default = +1)
  
  
"""
# Lets create a sequence of numbers
# starts at 0 default, 5 not inclusive
for num in range(5):
    print(num)

# Lets create a sequence of numbers 
# starts at 1, 5 not inclusive
for num in range(1,5):
    print(num)

# Lets create a sequence of numbers 
# with increment step of 3
for num in range(0,20,3):
    print(num)

# Lets create a reverse sequence of numbers 
# with increment step of 3
for num in range(20,0,-2):
    print(num)

# Lets use range for Iteration
# using range we will iterate through 
# fruits list
fruits=["Apple","Banana","Grapes","Orange"]

for i in range(len(fruits)):
    print(fruits[i])



