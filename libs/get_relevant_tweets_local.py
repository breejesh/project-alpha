import tweepy
import pyrebase
from connection import db, api
import json
import re

users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]

def combination(s):
    return [[s[j] for j in xrange(len(s)) if (i&(1<<j))] for i in xrange(1<<len(s))]

def load_data():
    tweet = {}
    try:
        for user in users:
            user_tweet = {}
            print user
            try:
                json_data = open('../data/' + user.lstrip('@') + '.json').read()
            except Exception, e:
                json_data = open('data/' + user.lstrip('@') + '.json').read()
            data = json.loads(json_data)
            for i in range(len(data)):
                user_tweet[data[i]['id']] = data[i]['text']
        tweet[user] = user_tweet
    except Exception, e:
        print e
        tweet = {}
        return tweet            
    return tweet

# Returns a list of relevant tweets as list based on keyword
def find_all(keywords):
    # Create a search pattern
    relevant_tweets = []
    words = combination(keywords)
    for user in users:
        print user
        flag = 0
        try:
            i = len(words)
            print i
            while(True):
                if(i == 1):
                    break
                i -= 1
                for tweet_id, tweet in data[user].iteritems():
                    # In each tweets find keywords
                    if all(keyword in tweet for keyword in words[i]):
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
print find_all(["donald", "trump", "dead"])