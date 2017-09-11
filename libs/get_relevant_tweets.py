import tweepy
import pyrebase
from connection import db, api
import re

users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@asharma","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

# Returns a list of relevant tweets as list based on keyword
def find_all(keywords):
    # Create a search pattern
    relevant_tweets = []
    search_pattern = keywords[0]
    for i in range(1, len(keywords)):
        search_pattern += ('|' + keywords[i])
    for user in users:
        print user
        data = db.child("users").child(user).get()
        try:
            for i, (key, value) in enumerate(data.val().iteritems()):
                # In each tweets find keywords
                if(re.search(search_pattern, value, flags=re.IGNORECASE)):
                    relevant_tweets.append(value)
<<<<<<< HEAD
                    break
=======
                    print value
>>>>>>> cf550a17829deaef848d1f11852ecb07381254cf
        except Exception, e:
            print str(user) + " not found"
    return relevant_tweets


