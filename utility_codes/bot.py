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
users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@AmolSharmaWsj","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@Rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

def process_new_tweets():
    # Get tweet for particular screen name
    data = db.child("users").child("@sagarikaghose").get()
    print type(data.val())
    print data.val()
    # for item in data.val():
    #    print item
    exit(0)    
    for user in users:
        # Fetch  tweet id from Firebase
        data = db.child("users").child(user).get()
        for page in Cursor(api.user_timeline, screen_name=user.lstrip('@'), count=200).pages(20):
            for tweet  in page:
                # If exists in Firebase
                for key in data.val():
                    if tweet.id == key:
                        print "In Firebase"
                        continue
                # Firebase code here
                recent_tweet = {tweet.id : tweet.text}
                db.child("users").child(user).push(recent_tweet)

def main():
    # Get data from twitter
    while True:
		process_new_tweets()
		time.sleep(10)

if __name__=='__main__':
    main()
