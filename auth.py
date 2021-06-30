# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:58:47 2021

@author: greed
"""

import tweepy

def auth():
    CONSUMER_KEY = '5Ly7e8KM4BHn5qQQtTE4Cl7FY'
    CONSUMER_SECRET = 'F9PYqqHlm6NPrco7fANXjs5X1iKbKj841wfYDxzJFuqC1W7fyQ'
    ACCESS_KEY ='1376542724082561032-Az6l5bAO1qkhVf1CfGtH733n3amtCz'
    ACCESS_SECRET = 'rn4qvoQUpOu4vaBuhPOGbiAshFTTL2Jbom8tkh1NDEby7'
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api,auth
