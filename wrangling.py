import os

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --progress --max-results 2 twitter-search \"covid since:2020-01-01 until:2022-11-01 lang:id\" > user-tweets.json")