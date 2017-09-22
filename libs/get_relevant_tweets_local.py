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
            print user
            try:
                json_data = open('../data/' + user.lstrip('@') + '.json').read()
            except Exception, e:
                json_data = open('data/' + user.lstrip('@') + '.json').read()
            data = json.loads(json_data)
            for i in range(len(data)):
                tweet[data[i]['id']] = data[i]['text']
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
        data = load_data()
        try:
            i = len(words)
            while(True):
                if(i == 1):
                    break
                i -= 1
                for j, (id, tweet) in enumerate(data.val().iteritems()):
                    # In each tweets find keywords
                    if all(keyword in tweet for keyword in words[i]):
                        relevant_tweets.append(tweet)
                        print tweet
                        flag = 1
                    if flag == 1:
                        break
            if flag == 0:
                relevant_tweets.append(' ')
        except Exception, e:
            print str(user) + " not found"
    return relevant_tweets

if __name__ == '__main__':
    load_data()