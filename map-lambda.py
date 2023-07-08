#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 02:37:46 2023

@author: angelateyvi
"""

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda spell: spell + "!!!", spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list= list(shout_spells)

# Print the result
print(shout_spells_list)