#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 18:31:40 2023

@author: angelateyvi
"""

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Replace print with return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell = shout('con')

# Print yell
print(yell)