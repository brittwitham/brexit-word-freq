import os
import pandas as pd
import itertools
import collections
from datetime import datetime
import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx
import pymongo

import warnings
warnings.filterwarnings("ignore")

client = pymongo.MongoClient(os.environ.get("DATABASE"))
db = client.politics.brexit

# Twitter keys #
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Twitter Authorization #
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Query variables #
search_term = "#brexit -filter:retweets"
date_since = "2020-12-01"
todays_time = datetime.now().strftime("%d %H:%M")
todays_day = datetime.now().strftime('%A')

# Function to remove URLS #
def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

# Twitter request #
tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since=date_since).items(300)

# Gather tweets and remove URLs #
all_tweets = [tweet.text for tweet in tweets]
all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]

# Create a list of lists containing lowercase words for each tweet #
words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]

# List of all words across tweets #
all_words_no_urls = list(itertools.chain(*words_in_tweet))

# Create counts of each word across all tweets #
counts_no_urls = collections.Counter(all_words_no_urls)

# Instantiate stop words #
stop_words = set(stopwords.words('english'))

# Remove stop words from results #
tweets_nsw = [[word for word in tweet_words if not word in stop_words]
              for tweet_words in words_in_tweet]
all_words_nsw = list(itertools.chain(*tweets_nsw))
counts_nsw = collections.Counter(all_words_nsw)

# Defines collection words #
collection_words = [
    'brexit',
    'would',
    'get',
    'time',
    'like',
    'uk',
    'eu'
]

# Removes collection words #
tweets_nsw_nc = [[w for w in word if not w in collection_words]
                 for word in tweets_nsw]

# Flatten list of words in clean tweets
all_words_nsw_nc = list(itertools.chain(*tweets_nsw_nc))
# Create counter of words in clean tweets
counts_nsw_nc = collections.Counter(all_words_nsw_nc)
var = counts_nsw_nc.most_common(20)

wordsdict = dict(var)

data = {
    "timestamp": datetime.now().strftime("%d %H:%M"),
    "words": wordsdict
}

x = db.insert_one(data)
print(x.inserted_id)
