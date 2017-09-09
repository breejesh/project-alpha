import tweepy
import threading 
import re
import time
import collections
from tweepy import Cursor
import pyrebase
from connection import db, api

user = '@sagarikaghose'

def get_tweets():
    # get all data from twitter for a user
    i = 0
    data = {}
    tweet_of_user = {}
    for page in Cursor(api.user_timeline, screen_name=user.lstrip('@'), count=200).pages(20):
        print "Processing page..." + str(i)
        i += 1
        # Process each page
        for tweet in page:
            tweet_of_user[tweet.id] = tweet.text
    data["users/" + user + "/"] = tweet_of_user
    db.update(data)


def main():
    # Get data from twitter
    get_tweets()

if __name__=='__main__':
    main()
