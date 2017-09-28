import tweepy
from threading import Timer
from datetime import datetime
import re
import time
import collections
from tweepy import Cursor
import pyrebase
from connection import db, api
import pickle

users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]

def load_data():
    tweet = {}
    print "Loading pickle file.."
    try:
        with open('data/tweet_data.pickle', 'rb') as handle:
            tweet = pickle.load(handle)
    except:
        with open('/home/himanhsu/Desktop/Hackocracy/project_alpha/data/tweet_data.pickle', 'rb') as handle:
            tweet = pickle.load(handle)        
    print "Pickle file loaded!"
    return tweet

def process_new_tweets():
    i = 0
    data = load_data() 
    for user in users:
        if i == 0:
            i+=1
            continue
        # Fetch  tweet id from Firebase
        print user 
        print len(data[user])
        flag = 0
        try:
            for page in Cursor(api.user_timeline, screen_name=user.lstrip('@'), count=200).pages(20):
                for tweet in page:
                    # If exists in Firebase
                    for tweet_id, text in data[user].iteritems():
                        if tweet.id == tweet_id:
                            print "In Pickle File"
                            flag = 1 
                            break
                    text = tweet.text
                    text = text.lower().encode('utf-8')
                    text = re.sub(r"http\S+", '', text)
                    text = re.sub("[^a-zA-Z0-9\n]", " ", text)
                    data[user][tweet.id] = tex
        except Exception, e:
            print e
        with open('data/tweet_data.pickle', 'wb') as handle:
            print "Saving pickle file..."
            pickle.dump(tweet, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print "Pickle file saved!"


def bot():
    x = datetime.today()
    y = x.replace(day=x.day + 2, hour=2, minute= 0 , second=0, microsecond=0)
    print x, y
    delta_t = y-x
    print delta_t
    secs = delta_t.seconds + 1
    t = Timer(secs, process_new_tweets)
    t.start()
    return y

y = bot()
while True:    
    time.sleep(7199)
    if datetime.today() > y:
        y = bot()
    