import tweepy
import threading 
import re
import time
import collections
import tweepy import Cursor

# Connect to Twitter
consumer_key = 'jDTkvPn7dvRO1ZaC3wz6Yv5vv'
consumer_secret = 'SkcHH6uCMNZkEryUhooMOqZeYUwNDcjJZZyoCNUmc4tE8oszYT'
access_token = '822855599457112064-ttTgq1HKm9ImytpZyLsdI54tKqHunRD'
access_token_secret = 's2xBzW2q1sTfXnjbiynBkRdlX2CZwv9wOlsiPLAiFGCJS'
# Authuentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@AmolSharmaWsj","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@Rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]

def process_new_tweets():
    # Get tweet for particular screen name
    for user in users:
        for page in Cursor(api.user_timeline, screen_name=user.lstrip('@', count=200).pages(20):
            for tweet  in page:
                # Replicate this in firebase
                # cur = con.execute('SELECT * FROM read_tweets where tweet_id = ?', (tweet.id,)) -> Firebase
		        # If exists in Firebase
                if cur.fetchone() is not None:
			        continue
                # Firebase code here
        
def main():
    # Get data from twitter
    while True:
		process_new_tweets()
		time.sleep(10)

if __name__=='__main__':
    main()
