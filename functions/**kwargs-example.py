#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 01:34:28 2023

@author: angelateyvi
"""
#import pandas library
import pandas as pd

#import the tweet data frame
tweets_df = pd.read_csv("tweets.csv")

# Define count_entries()
def count_entries(tweets_df, col_name="lang"):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = tweets_df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, col_name="lang")

# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name="source")

# Print result1 and result2
print(result1)
print(result2)