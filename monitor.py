# this code programmatically monitors for certain hashtags and tweets a response
#
# requires tweepy to be installed via pip
# navigate to python27 folder
# download and save pip into python27 folder from:
#      https://raw.github.com/pypa/pip/master/contrib/get-pip.py
#      or, there should be a copy of it on my github
# install pip by running: python get-pip.py
# install tweepy by running: Scripts\pip install tweepy

import tweepy
import time 

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

# create custom listener to process tweets
class CustomStreamListener( tweepy.StreamListener ):

    def on_status( self, status ):
        print( 'Tweet text: ' + status.text.encode('utf-8'))
        print( 'Tweet user: ' + status.user.screen_name)
        for hashtag in status.entities['hashtags']:
           print(hashtag['text'])
        api.update_status('AutoResponse from #CodeSaints: Thanks for the tweet @' + status.user.screen_name + ' %s' % (time.strftime("%H:%M:%S")))

    def on_error( self, status_code ):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
    listener = CustomStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = tweepy.Stream(auth, listener)
    stream.filter(follow=[],track=['#codesaintstest'])