import pyrebase
import json
import os
import sys
import re
# from connection import db

print "Starting.."
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
print "Clearing database.."
db.update(clear_stuff)
print "Database cleared!"
print "Next.."
def process_text(text):
    text = text.lower().encode('utf-8')
    text = re.sub(r"http\S+", '', text)
    text = re.sub("[^a-zA-Z0-9\n]", " ", text)
    return text

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
                db_item = [process_text(data[i]['text']), data[i]['likes'], data[i]['retweets']]
                tweet[data[i]['id']] = db_item
                # item = {data[i]['id'] : db_item}
            db.child("users").child(f.rstrip('.json')).set(tweet)
            print "Done"
except Exception, e:
    print e
print "Done"
print j
