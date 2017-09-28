import tweepy
import pyrebase
from connection import db, api
import json
import re
import pickle
users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]

def combination(s):
    return [[s[j] for j in xrange(len(s)) if (i&(1<<j))] for i in xrange(1<<len(s))]

def load_data():
    tweet = {}
    print "Loading pickle file.."
    try:
        with open('data/tweet_data.pickle', 'rb') as handle:
            tweet = pickle.load(handle)
    except:
        with open('/home/ryuzaki/mysite/data/tweet_data.pickle', 'rb') as handle:
            tweet = pickle.load(handle)        
    print "Pickle file loaded!"
    return tweet

def find_all(keywords):
    relevant_tweets = []
    for user in users:
        print user
        flag = 0
        user_tweet = {}
        min_intersection = 2 
        try:
            #print words[i - 1]
            for tweet_id, tweet in data[user].iteritems():
                # In each tweets find keywords
                new_tweet = tweet.split(" ")
                matched_keywords = len(list(set(new_tweet).intersection(keywords))) 
                if matched_keywords not in new_tweet:
                    if matched_keywords >= min_intersection: 
                        user_tweet[matched_keywords] = tweet
                        flag = 1
            if flag == 0:
                relevant_tweets.append(' ')
            else:
                relevant_tweets.append(user_tweet[max(user_tweet)])
        except Exception as e:
            print str(user) + " caused " + str(e.message)
    print relevant_tweets
    return relevant_tweets

data = load_data()

'''
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
                #print words[i - 1]
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
'''
