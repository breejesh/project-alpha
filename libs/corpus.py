import nltk.corpus
import string

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def remove_stopwords(query):
    query = query.split(' ')
    keywords = [token.lower() for token in query if token.lower() not in stopwords]
    return keywords
