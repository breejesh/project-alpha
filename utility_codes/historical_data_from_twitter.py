import tweepy
import threading 
import re
import time
import collections
from tweepy import Cursor
import pyrebase
from connection import db, api

# AmolSharmaWsj->acoount suspended 
users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@asharma","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

def get_tweets():
    # get all data from twitter for a user
    data = {}
    # for user in users:
    for user in users:
        i = 0
        tweet_of_user = {}
        try:
            for page in Cursor(api.user_timeline, screen_name=user.lstrip('@'), count=200).pages(50):
                print "Processing page..." + str(i) + " of " + str(user)
                i += 1
                # Process each page
                for tweet in page:
                    tweet_of_user[tweet.id] = tweet.text
            data["users/" + user + "/"] = tweet_of_user
            db.update(data)
        except Exception, e:
            print str(user) + "not found"

def main():
    # Get data from twitter
    get_tweets()

if __name__=='__main__':
    main()
