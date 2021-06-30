# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:58:47 2021

@author: greed
"""

import tweepy

def auth():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY =''
    ACCESS_SECRET = ''
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api,auth
