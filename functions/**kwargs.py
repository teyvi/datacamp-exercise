#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 01:18:02 2023

@author: angelateyvi
"""

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for name, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(name,"=",value )

    print("\nEND REPORT")

# First call to report_status()


# Second call to report_status()
report_status(name='anakin', affiliation="sith lord", status="deceased")