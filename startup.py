#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import json
from logging.config import dictConfig
import tweepy
from logging_settings import logging_config

import logging
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


def initiate():
    __extend_tweepy__()
    dictConfig(logging_config)
    logger.debug("Initiation completed")
