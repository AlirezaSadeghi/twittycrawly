#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


import json
from collections import Counter
import logging

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.models import Status

from lib import preprocess
from stream_listeners import MyListener

logger = logging.getLogger(__name__)


def __extend_tweepy__():

    @classmethod
    def parse(cls, api, raw):
        status = cls.first_parse(api, raw)
        setattr(status, 'json', json.dumps(raw))
        return status

    tweepy.models.Status.first_parse = tweepy.models.Status.parse
    tweepy.models.Status.parse = parse
    tweepy.models.User.first_parse = tweepy.models.User.parse
    tweepy.models.User.parse = parse


consumer_key = 'L2KKmdQ0Ffx4bYHex6GBcOs91'
consumer_secret = 'psQx9YWcHuG17PWAGpVad9PKlqfXXsgbI9DuL7ZqSAxta6LocH'
access_token = '1940603868-qtOkIYxCxWTzSAsSnTq7irStPKDUr0pwKB89jUd'
access_secret = 'a7YBTDaD6GgbnrECGzBBVND2HyS4pofFXP8OKPrf2bo7v'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


from nltk.corpus import stopwords
import string

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
    __extend_tweepy__()

    # twitter_stream = Stream(auth, MyListener())
    # twitter_stream.filter(track=['#lyon', '#Kuwait'])
    result = api.search(**{
        'q': '#IranTalks',
        'count': 100,
    })
    print(len(result))
    for item in result:
        print(item.json)
