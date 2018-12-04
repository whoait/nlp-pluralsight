import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# tokenize text
text = "How high-tech suppliers are responding to the hyperscaler opportunity? To win in the hyperscaler market, tech vendors must take an entirely new approach."
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
print('tokenize text is bellow')
print(sents)

words=[word_tokenize(sent) for sent in sents]
print(words)

#remove Stopwords
from nltk.corpus import stopwords 
from string import punctuation
customStopWords=set(stopwords.words('english')+list(punctuation))
wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

#indentifying Bigram
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
print(sorted(finder.ngram_fd.items()))

print('//////////////////')
print('//////////////////')
print('//////////////////')
#Stemming and POS Tagging


text2 = "Over the last three years, estimates suggest, hyperscalers have spent $185 billion on data centers about $75 billion in 2017 alone."
from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text)]
print(stemmedWords)

print(nltk.pos_tag(word_tokenize(text2)))

print('//////////////////')
print('//////////////////')
print('//////////////////')

# //Disambiguating Word Meanings
from nltk.corpus import wordnet as wn
for ss in wn.synsets('hello'):
    print(ss, ss.definition())

from nltk.wsd import lesk
sense1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"),'bass')
print(sense1, sense1.definition())

sense2 = lesk(word_tokenize("This sea bass was really hard to catch"),'bass')
print(sense2, sense2.definition())

