import gensim
from gensim.models.keyedvectors import KeyedVectors

print "Loading..."
model = KeyedVectors.load_word2vec_format('models/glove_twitter_27B_25d.txt', binary=False)
print "Loaded"
print "Predicting.."
try:
    print model.similarity('woman', 'man')
except:
    print 0.0
try:
    print model.similarity('dead', 'alive')
except:
    print 0.0
try:
    print model.similarity('PM', 'Modi')
except:
    print 0.0
try:
    print model.similarity('pokemon', 'goku')
except:
    print 0.0
print "Done"
