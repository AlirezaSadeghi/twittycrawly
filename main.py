#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

from constants import consumer_key, consumer_secret, access_token, access_secret
from startup import initiate
from stream_listeners import MyListener

import logging
logger = logging.getLogger(__name__)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# punctuation = list(string.punctuation)
# stop = stopwords.words('english') + punctuation + ['rt', 'via']
# fname = 'mytweets.json'
# with open(fname, 'r') as f:
#     count_all = Counter()
#     for line in f:
#         tweet = json.loads(line)
#         all_terms = [term for term in preprocess(tweet['text']) if term not in stop]
#         count_all.update(all_terms)
#
#     print(count_all.most_common(5))


# Count terms only once, equivalent to Document Frequency
# terms_single = set(all_terms)
# Count hashtags only
# terms_hash = [term for term in preprocess(tweet['text'])
#               if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
# terms_only = [term for term in preprocess(tweet['text'])
#               if term not in stop and
#               not term.startswith(('#', '@'))]
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if
              # we pass a list of inputs


if __name__ == '__main__':
    initiate()
    # twitter_stream = Stream(auth, MyListener())
    # twitter_stream.filter(track=['#IranTalks'])
    # result = api.search(**{
    #     'q': '#IranTalks',
    #     'count': 100,
    # })
    # print(len(result))
    # for item in result:
    #     print(item.json)
