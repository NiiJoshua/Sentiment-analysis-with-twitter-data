# Importing modules
import tweepy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Add your credentials
consumer_key = "xxxx"
consumer_secret = "xxxx"
access_token = "xxxx"
access_token_secret = "xxxx"

# initializing initial credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)