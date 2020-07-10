import json
import csv
import tweepy
import re

# Twitter authentication (insert your own credentials here)
# consumer_key, consumer_secret
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# access_token, access_token_secret
access_token = ""
access_token_secret = ""
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#insert search terms here
search_terms = ""
# I didn't want to include the search terms in the resulting word cloud
terms_split = search_terms.split()

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# max 100 tweets
tweets = tweepy.Cursor(api.search, q=search_terms, lang="en").items(100)

cloud = ""
for each in tweets:
    cloud = cloud + each.text

stopwords=["https", "co"]

# add the search terms as stop words
for word in terms_split:
    stopwords.append(word)

cloud = WordCloud(background_color="white", stopwords=STOPWORDS.union(stopwords), width=1800, height=1400).generate(cloud)
plt.figure(figsize = (12, 6))
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
plt.show()