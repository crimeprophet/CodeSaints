# requires tweepy to be installed via pip
# navigate to python27 folder
# download and save pip into python27 folder from:
#      https://raw.github.com/pypa/pip/master/contrib/get-pip.py
# install pip by running: python get-pip.py
# install tweepy by running: Sripts\pip install tweepy

import tweepy

# enter your authentication details below (see dev.twitter.com)
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# create authentication token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# get API handler
api = tweepy.API(auth)

# get text to tweet - should add error check for tweet length
tweet = raw_input( "Enter text to tweet: " )

print "Sending tweet ", tweet
api.update_status('Tweet via python #CodeSaints: ' + tweet)
