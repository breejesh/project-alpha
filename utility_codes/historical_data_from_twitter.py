import tweepy
import threading 
import re
import time
import collections
from tweepy import Cursor

# Consumer keys
consumer_key = 'jDTkvPn7dvRO1ZaC3wz6Yv5vv'
consumer_secret = 'SkcHH6uCMNZkEryUhooMOqZeYUwNDcjJZZyoCNUmc4tE8oszYT'
# Access token
access_token = '822855599457112064-ttTgq1HKm9ImytpZyLsdI54tKqHunRD'
access_token_secret = 's2xBzW2q1sTfXnjbiynBkRdlX2CZwv9wOlsiPLAiFGCJS'
# Establish connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# DB connect
api = tweepy.API(auth)

def process_page(page):
    i = 0
    for tweet in page:
        i += 1
    print i
    return i


def get_tweets():
    tot = 0
    for page in Cursor(api.user_timeline, screen_name='', count=200).pages(20):
        tot += process_page(page)
    print tot

def main():
    # Get data from twitter
    get_tweets()

if __name__=='__main__':
    main()
