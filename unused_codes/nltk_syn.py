from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
 
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
	#print word, tag
	wn_tag = penn_to_wn(tag)
	if wn_tag is None:
		return None
	try:
		return wn.synsets(word, wn_tag)[0]
	except:
		return None
 
def sentence_similarity(sentence1, sentence2):
	score, count = 0.0, 0
	sentence1 = pos_tag(word_tokenize(sentence1))
	sentence2 = pos_tag(word_tokenize(sentence2))
	print "Sentence"
	print sentence1, sentence2
	synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
	synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
	synsets1 = [ss for ss in synsets1 if ss]
	synsets2 = [ss for ss in synsets2 if ss]
	print "Synset"
	print synsets1, synsets2
	for synset in synsets1:
		best_score = max([synset.path_similarity(ss) for ss in synsets2])
		if best_score is not None:
			score += best_score
			count += 1
 
 	score /= count
	return score
 
sentences = [
    "Princess Kate Middleton is pregnant, claims friend."
]
 
focus_sentence = "Kate Middleton is  Pregnant"

def symmetric_sentence_similarity(sentence1, sentence2):
	return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2 

for sentence in sentences:
    print "SymmetricSimilarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, symmetric_sentence_similarity(focus_sentence, sentence))
    print 
 