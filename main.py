from datetime import timedelta, datetime
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import tweepy
import snscrape.modules.twitter as sntwitter

query = "covid since:2020-01-01 until:2022-11-01 lang:id"
tweets = []
limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user, tweet.content, tweet.id])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Tweet ID'])
print(df)

# to save to csv
df.to_csv('tweets_covid.csv')