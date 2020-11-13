'''
    Retweet bot for Twitter, using Python and Tweepy.
    Retweet from specific user.
    Author: Sergio Villaverde.
    Date: 11/11/2020
'''

import tweepy
from time import sleep

'''
Import your keys from the keys.py file.
Make sure your keys.py is in the same directory as this script.
'''
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, id=account_name).items(5):
    try:
        print('\nRetweet bot found tweet by @' + account_name + '. ' + 'Attempting to retweet.')
        
        tweet.retweet()
        print('Retweet published successfully.')
        
        '''
        Sleep(180) is measured in seconds.
        Change it to amount of seconds you want to have between retweets.
        Read Twitter's rules about spam!
        '''
        sleep(180)
    
    # Basic error handling. Will inform if it fails. 
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
        
    except StopIteration:
        break