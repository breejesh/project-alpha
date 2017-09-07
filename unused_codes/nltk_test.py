import nltk.corpus
import nltk.tokenize
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

# Create tokenizer and stemmer
tokenizer = nltk.tokenize.casual.TweetTokenizer()
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
stemmer = nltk.stem.snowball.SnowballStemmer('english')

def token_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    print tokens_a, tokens_b
    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    return ratio

def stem_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    stems_a = [stemmer.stem(token) for token in tokens_a]
    stems_b = [stemmer.stem(token) for token in tokens_b]
    print stems_a, stems_b
    # Calculate Jaccard similarity
    ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))
    return ratio

def lemma_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    print lemmae_a, lemmae_b
    # Calculate Jaccard similarity
    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    return ratio

print "Lemma"
print lemma_match("Goa is a state", "Goa is a city")
print lemma_match("Goa is a state", "India has a state named goa")
print lemma_match("Donald Trump is alive", "Donald Trump is dead")
print lemma_match("Donald Trump is not dead", "Donald Trump is dead")

print "Stem"
print stem_match("Goa is a state", "Goa is a city")
print stem_match("Donald Trump is alive", "Donald Trump is dead")
print stem_match("Goa is a state", "India has a state named goa")
print stem_match("Donald Trump is not dead", "Donald Trump is dead")

print "Token"
print token_match("Goa is a state", "Goa is a city")
print token_match("Goa is a state", "India has a state named goa")
print token_match("Donald Trump is alive", "Donald Trump is dead")
print token_match("Donald Trump is not dead", "Donald Trump is dead")
