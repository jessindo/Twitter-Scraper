# TwitterScraper.py

- Created a Python program that scrapes Tweets related to certain search terms/hashtags and visualises the data as a word cloud
- Developed using the Twitter API and various Python libraries (nltk, numpy)

## To run:
1. Include your own Twitter authentication credentials and access tokens
```
Twitter authentication (insert your own credentials here)
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = ""
access_token_secret = ""
auth.set_access_token(access_token, access_token_secret)
```

