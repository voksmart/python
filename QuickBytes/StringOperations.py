# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:35:40 2019

@author: Mohit
"""
# String Assignment
str1 = "Hello" 
str2 = "John"

# Checking String Length
print("Length of String is :",len(str1))

# String Concatenation (join)
print(str1 + " "+str2)

# String Formatting
# inserting name of guest after welcome
print("Welcome %s.Enjoy your stay"%(str2))

# Changing String Case
guestname = "John Smith"
# converts string to lower case
print(guestname.lower())

# converts string to UPPER case
print(guestname.upper())

# converts string to title case
# First letter of every word is capital
print(guestname.title())

# Stripping White Spaces 
# string below has leading and trailing 
# white space
message = "    Good Morning John   "

# remove all leading and trailing whitespace
print(message.strip())

# remove leading white space
print(message.lstrip())

# remove trailing white space
print(message.rstrip())

# String Formatting 
# Using format{} function
guest = "John Smith"
city = "New York"
mobile="iphone"
price=199.234

# Simple Formatter with place holders
print("Hello {}! Welcome to {}".format(guest,city))
print("My {} cost me {}".format(mobile,price))

# With positional arguments
# Note changed position in format function
print("My {1} cost me {0}".format(price,mobile))

# controlling display with format specifiers
print("My {1:s} cost me {0:.2f}".format(price,mobile))

# Formatting using fstring
print(f"Hello {guest}. Welcome to {city}")
print(f"My new {mobile} cost me {price:.2f}")















