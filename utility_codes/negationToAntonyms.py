import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize

antonymSet = {}

# Build from local data set
def buildAntonymSet():
    f = open('../data/antonymsVocab.csv', 'rU')
    for line in f:
        cell = line.split(",")
        antonymSet[cell[0]] = cell[1].rstrip('\n')
        antonymSet[cell[1].rstrip('\n')] = cell[0]


class AntonymReplacer(object):
  def replace(self, word, pos=None):
    antonyms = set()
    for syn in wordnet.synsets(word, pos=pos):
      for lemma in syn.lemmas():
        for antonym in lemma.antonyms():
          antonyms.add(antonym.name)
    if len(antonyms) == 1:
      return antonyms.pop()
    else:
        if word.lower() in antonymSet:
            return antonymSet[word.lower()]
        else:
            return None

  def replace_negations(self, sent):
    i, l = 0, len(sent)
    words = []
    while i < l:
      word = sent[i]
      if (word == 'not' or word == 'never') and i+1 < l:
        ant = self.replace(sent[i+1])
        if ant:
          words.append(ant)
          i += 2
          continue
      words.append(word)
      i += 1
    return words



def main():
    buildAntonymSet()
    replacer = AntonymReplacer()
    sent = "Donald Trump is not alive"
    sent_tokenized = word_tokenize(sent)
    print(replacer.replace_negations(sent_tokenized))
    
if __name__ == '__main__':
    main()