import tweepy
import pyrebase
from connection import db, api
import json
import re
from connection import db

users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]
def combination(s):
    return [[s[j] for j in xrange(len(s)) if (i&(1<<j))] for i in xrange(1<<len(s))]

def load_data():
    tweet = {}
    try:
        for user in users:
            user_tweet = {}
            try:
                data = db.child("users").child(user.lstrip('@')).get()
            except Exception, e:
                print "Firebase Error"
            for j, (id, text) in enumerate(data.val().iteritems()):
                    # In each tweets find keywords
                    print id, text[0]
                    user_tweet[id] = text[0]
            tweet[user] = user_tweet
    except Exception, e:
        print e
    print tweet
    exit(0)
    return tweet

# Returns a list of relevant tweets as list based on keyword
def find_all(keywords):
    # Create a search pattern
    relevant_tweets = []
    words = combination(keywords)
    for user in users:
        print user, len(data[user])
        flag = 0
        try:
            i = len(words)
            while(True):
                print words[i - 1]
                if(i == 1):
                    break
                i -= 1
                if len(words[i]) == 1:
                    continue
                for tweet_id, tweet in data[user].iteritems():
                    # In each tweets find keywords
                    new_tweet = tweet.split(" ")
                    if set(words[i]) < set(new_tweet) :
                        relevant_tweets.append(tweet)
                        print tweet
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                relevant_tweets.append(' ')
        except Exception as e:
            print str(user) + " caused " + str(e.message)
    return relevant_tweets

data = load_data()
