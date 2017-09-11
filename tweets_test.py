from libs import get_relevant_tweets

ans =  get_relevant_tweets.find_all(["donald", "trump", "dead"])
for x in ans:
    print x