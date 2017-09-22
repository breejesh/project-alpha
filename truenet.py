from libs import other_analysis
from libs import corpus
from libs import sentence_comparison as sc
from libs import get_relevant_tweets_local as tweets_db

def analyze(query):
    keywords = corpus.remove_stopwords(query)
    print keywords
    tweets = tweets_db.find_all(keywords)
    values = []
    for tweet in tweets:
        values.append(sc.my_sentence_similarity(query, tweet))
        print values
    mean_value = mean(values)
    percentage = mean_value * 100 # Some processing
    return percentage
    #return other_analysis.analyze(query, percentage)

def mean(values):
    avg = [8, 6, 7, 5, 8, 8, 4, 5]
    sum = 0
    count = 0
    for x in values:
        sum += x
        count += 1
    if count == 0:
        return 0
    return float(sum)/count

'''
def match_sentences(query, tweets):
    values = []
    for tweet in tweets:
        values.append(sentence_comparison(query, tweet))
    return values
'''
