from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import nltk.corpus
import nltk.tokenize
import nltk.stem.snowball
import string
from gensim.models.keyedvectors import KeyedVectors

# Load word2vec model
print "Loading model..."
model = KeyedVectors.load_word2vec_format('data/glove_twitter_27B_25d.txt', binary=False)
print "Loading complete..."

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

 # Create tokenizer and stemmer
tokenizer = nltk.tokenize.casual.TweetTokenizer()
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
stemmer = nltk.stem.snowball.SnowballStemmer('english')

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0].lemmas()[0].name()
    except:
        if tag == 'NNP' or tag == 'NN':
            return word
        return None

def ttsynset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None

def word_semantics(sentence, word, threshold = 0.6):
    best_score = 0
    for s in sentence:
        s = str(s)
        try:
            score = model.similarity(word, s)
        except:
            score = 1
        if score > best_score:
            best_score = score
    return best_score >= threshold

def word_relevant_to_sentence(sentence, word, threshold = 0.6):
    sentence = pos_tag(word_tokenize(sentence))
    word = pos_tag(word_tokenize(word))
    synsets = [ttsynset(*tagged_word) for tagged_word in sentence]
    synsets = [ss for ss in synsets if ss]
    synsetsW = [ttsynset(*tagged_word) for tagged_word in word]
    synsetsW = [ss for ss in synsetsW if ss]
    print synsetsW
    try:
        best_score = 0
        for ss in synsets:
            print synsetsW[0], ss, synsetsW[0].wup_similarity(ss) 
            if synsetsW[0].wup_similarity(ss) > best_score:
                best_score = synsetsW[0].wup_similarity(ss)
        return best_score >= threshold
    except:
        return True

def my_sentence_similarity(sentence1, sentence2):
    # sentence 1 is always to source
    source = sentence1.lower()
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    #print sentence1, sentence2
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    tokens_a = [token.lower() for token in synsets1 \
                    if token.lower() not in stopwords]
    tokens_b = [token.lower() for token in synsets2 \
                    if token.lower() not in stopwords if word_semantics(tokens_a, token.lower())]
    #print tokens_a, tokens_b
    stems_a = [stemmer.stem(token) for token in tokens_a]
    stems_b = [stemmer.stem(token) for token in tokens_b]
    #print stems_a, stems_b
    # Calculate Jaccard similarity
    ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))
    return ratio

def remove_stopwords(query):
    keywords = [token.lower() for token in query if token.lower() not in stopwords]
    print keywords