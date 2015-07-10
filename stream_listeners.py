#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from tweepy import StreamListener

import logging
logger = logging.getLogger(__name__)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                logger.info(data)
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True