import pyrebase
import json
import os
import sys
# from connection import db

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
clear_stuff = {}
clear_stuff["users"] = 0
db.update(clear_stuff)
print "db cleared"
j = 0
try:
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print f
        if f.find(".json") != -1:	
            json_data = open(f).read()
            data = json.loads(json_data)    
            # all_tweets = {}
            tweet = {}
            for i in range(len(data)):
                j += 1
                if j % 5000 == 0:
                    print j
                db_item = [data[i]['text'], data[i]['likes'], data[i]['retweets']]
                tweet[data[i]['id']] = db_item
                # item = {data[i]['id'] : db_item}
            db.child("users").child(f.rstrip('.json')).set(tweet)
            print "Done"
    '''
    all_tweets["users/" + user + "/"] = tweet
    print "Updating.."
    db.update(all_tweets)
    print "Updated!"
    '''
except Exception, e:
    print e
print "Done"
print j
