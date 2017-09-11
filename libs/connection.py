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