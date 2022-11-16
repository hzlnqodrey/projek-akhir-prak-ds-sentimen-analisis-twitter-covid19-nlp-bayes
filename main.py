from datetime import timedelta, datetime
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import tweepy
import snscrape.modules.twitter as sntwitter

# Get All Covid Sentiment Data from January 1st, 2020 until November 1st, 2022
query = "covid since:2020-01-01 until:2022-11-01 lang:id"
limit = 100000 # limit 50k rows
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([
            tweet.date,
            tweet.username,
            tweet.content
        ])

filename = 'tweets_covid_dataset_50k_raw_noindex.csv'
tweets_df = pd.DataFrame(tweets, columns=['Tanggal', 'Username', 'Text'])
tweets_df.to_csv(filename, index=False)
print('Scraping has completed!')