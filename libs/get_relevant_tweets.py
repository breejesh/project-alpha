import tweepy
import pyrebase
from connection import db, api
import re

users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@asharma","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

def combination(s):
    return [[s[j] for j in xrange(len(s)) if (i&(1<<j))] for i in xrange(1<<len(s))]

# Returns a list of relevant tweets as list based on keyword
def find_all(keywords):
    # Create a search pattern
    relevant_tweets = []
    words = combination(keywords)
    for user in users:
        data = db.child("users").child(user).get()
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
                        break
        except Exception, e:
            print str(user) + " not found"
    return relevant_tweets


