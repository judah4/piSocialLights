import config
import twitter
# https://python-twitter.readthedocs.io/en/latest/getting_started.html
api = twitter.Api(consumer_key=config.twitter_consumer_key,
                  consumer_secret=config.twitter_consumer_secret,
                  access_token_key=config.twitter_access_token_key,
                  access_token_secret=config.twitter_access_token_secret)