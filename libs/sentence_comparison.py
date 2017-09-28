from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import nltk.corpus
import nltk.tokenize
import nltk.stem.snowball
import string

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
        #print word, tag
        if tag == 'NNP' or tag == 'NN' or tag == 'JJ':
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
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
    #print sentence1, sentence2
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    #print synsets1, synsets2
    if set(synsets1) <= set(synsets2):
        return 0.7
    tokens_a = [token.lower() for token in synsets1 \
                    if token.lower() not in stopwords]
    tokens_b = [token.lower() for token in synsets2 \
                    if token.lower() not in stopwords]

    if set(tokens_a) <= set(tokens_b):
        return 0.45
    stems_a = [stemmer.stem(token) for token in tokens_a]
    stems_b = [stemmer.stem(token) for token in tokens_b]
    #print stems_a, stems_b
    # Calculate Jaccard similarity
    ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))
    return ratio

def remove_stopwords(query):
    keywords = [token.lower() for token in query if token.lower() not in stopwords]
    print keywords