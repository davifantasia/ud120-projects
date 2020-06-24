from nltk.corpus import stopwords
sw = stopwords.words("english")
print '10th words in nltk stopwords list', sw[10]
print 'number of words in nltk stopwords list', len(sw)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print 'stem of responsiveness is:', stemmer.stem('responsiveness')
print 'stem of responsivity is:', stemmer.stem('responsivity')
print 'stem of unresponsive is:', stemmer.stem('unresponsive')

# tfIdf representation
# tf: term frequency
# Idf: inverse document frequency
