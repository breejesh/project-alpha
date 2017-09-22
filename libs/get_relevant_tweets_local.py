import tweepy
import pyrebase
from connection import db, api
import json
import re

users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]
avg = [8, 6, 7, 5, 8, 8, 4, 5]
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
                    tweet = tweet.lower()
                    tweet = re.sub("[@$%!,.#$^&'\"~`{}\[\]()]", " ", tweet)
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
