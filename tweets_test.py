from libs import get_relevant_tweets

ans =  get_relevant_tweets.find_all(["kate", "middleton", "pregnant"])
for x in ans:
    print x