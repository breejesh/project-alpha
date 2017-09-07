import tweepy
import threading 
import re
import time
import collections
from tweepy import Cursor

# Connect to Twitter
consumer_key = 'jDTkvPn7dvRO1ZaC3wz6Yv5vv'
consumer_secret = 'SkcHH6uCMNZkEryUhooMOqZeYUwNDcjJZZyoCNUmc4tE8oszYT'
access_token = '822855599457112064-ttTgq1HKm9ImytpZyLsdI54tKqHunRD'
access_token_secret = 's2xBzW2q1sTfXnjbiynBkRdlX2CZwv9wOlsiPLAiFGCJS'
# Authuentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def process_page(page):
    # Insert pages tweets to DB code here

def get_tweets():
    # get all data from twitter for a user
    for page in Cursor(api.user_timeline, screen_name='', count=200).pages(20):
        process_page(page)

def main():
    # Get data from twitter
    get_tweets()

if __name__=='__main__':
    main()
