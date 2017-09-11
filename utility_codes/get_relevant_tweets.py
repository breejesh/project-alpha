import tweepy
import pyrebase
from connection import db, api
import re
# Import libraby that will give key word as 
# from xyz_lib import keywords

users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@asharma","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

def get_relevant_tweets():
    # Create a search
    search_pattern = 'china|india'
    '''
    To be done based on how keywords are given
    for keyword in keywords:
    '''
    for user in users:
        data = db.child("users").child(user).get()
        print "Fetched data of " + str(user)
        print type(data.val())
        try:
            for i, (key, value) in enumerate(data.val().iteritems()):
                # In each tweets find keywords
                # print value
                if(re.search(search_pattern, value, flags=re.IGNORECASE)):
                    # Tweet is relevant 
                    pass
                    '''
                    do necessary action
                    '''
        except Exception, e:
            print "User not found"

if __name__ == '__main__':
    get_relevant_tweets()
    