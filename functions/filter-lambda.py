#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 02:58:56 2023

@author: angelateyvi
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda fellowship: len(fellowship) < 4, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)