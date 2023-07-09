#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:40:03 2023

@author: angelateyvi
"""

#import pandas library
import pandas as pd

#import the tweet data frame
tweets_df = pd.read_csv("tweets.csv")


# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)