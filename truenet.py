from libs import other_analysis
from libs import corpus
from libs import sentence_comparison as sc
from libs import get_relevant_tweets_pickle as tweets_db

def analyze(query):
    # Take keywords from input query
    keywords = corpus.remove_stopwords(query)
    print keywords

    # Search for relevant tweets, one per source
    tweets = tweets_db.find_all(keywords)

    # Compare the input with each relevant tweet
    values = []
    for tweet in tweets:
        values.append(sc.my_sentence_similarity(query, tweet))
    mean_value = mean(values)
    percentage = interpolate(mean_value * 100)

    # Source wise distribution
    sources = values 
    for i in range(0, len(sources)):
        sources[i] = sources[i] * 100 / 0.6
        if sources[i] > 100:
            sources[i] = 100

    print sources
    print percentage

    return other_analysis.analyze(query, percentage, values)
    #return percentage

def interpolate(mean_value):
    curr_range = 40.0                                                        # since we get 12 - 52 approx for all queries
    ans  = (mean_value - 12) / float(curr_range)       # value between 0-1
    ans *= 100                                                                      # percentage
    if ans < 0:
        ans = 0
    if ans > 100:
        ans = 100
    return ans

def mean(values):
    print values
    users = ["@timesofindia","@ndtv","@IndiaToday","@CNNnews18","@bsindia","@dna","@BreakingNews","@BBCBreaking"]
    avg = [80, 50, 75, 40, 70, 80, 20, 10]
    sources = []
    sum = 0
    count = 0
    denom = 0
    for x in values:
        sum += (x + 0.05) * avg[count]
        #sum += (x + 0.05)
        denom += avg[count]
        count += 1
    if count == 0:
        return 0
    return float(sum)/denom
    #return float(sum)/count
'''
def match_sentences(query, tweets):
    values = []
    for tweet in tweets:
        values.append(sentence_comparison(query, tweet))
    return values
'''
