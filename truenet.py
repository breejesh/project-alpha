from libs import other_analysis
from libs import corpus
#from libs import sentence_comparison
#from libs import himanshu

def analyze(query):
    keywords = corpus.remove_stopwords(query)
    print keywords
    #tweets = get_relevant_tweets(keywords)
    values = [6, 9, 1, 2, 3, 2, 5]
    mean_value = mean(values)
    percentage = mean_value # Some processing
    return other_analysis.analyze(query, percentage)

def mean(values):
    sum = 0
    count = 0
    for x in values:
        sum += x
        count += 1
    return float(sum)/count

'''
def match_sentences(query, tweets):
    values = []
    for tweet in tweets:
        values.append(sentence_comparison(query, tweet))
    return values
'''
