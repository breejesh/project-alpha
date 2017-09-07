import tweepy
import threading 
import re
import time
import collections
from tweepy import Cursor
import pyrebase

# Connect to Twitter
consumer_key = 'jDTkvPn7dvRO1ZaC3wz6Yv5vv'
consumer_secret = 'SkcHH6uCMNZkEryUhooMOqZeYUwNDcjJZZyoCNUmc4tE8oszYT'
access_token = '822855599457112064-ttTgq1HKm9ImytpZyLsdI54tKqHunRD'
access_token_secret = 's2xBzW2q1sTfXnjbiynBkRdlX2CZwv9wOlsiPLAiFGCJS'
# Authuentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Firebase connection
config = {
  "apiKey": " AIzaSyBHCAsvRwt-NMLsv4F1222SNXoQeyNQbzE ",
  "authDomain": "tweets11596.firebaseapp.com",
  "databaseURL": "https://tweets11596.firebaseio.com",
  "storageBucket": "tweets11596.appspot.com"
}
firebase = pyrebase.initialize_app(config)
firebase.auth()
db = firebase.database()
user = '@sagarikaghose'


def get_tweets():
    # get all data from twitter for a user
    i = 0
    data = {}
    tweet_of_user = {}
    for page in Cursor(api.user_timeline, screen_name=user.lstrip('@'), count=200).pages(50):
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
