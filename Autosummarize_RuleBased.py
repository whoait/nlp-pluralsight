import urllib2
from bs4 import BeautifulSoup
articleURL = "https://www.mckinsey.com/industries/high-tech/our-insights/how-high-tech-suppliers-are-responding-to-the-hyperscaler-opportunity/"

def getTextWaPo(url):
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,"lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    return text.encode('ascii', errors='replace').replace("?"," ")
text = getTextWaPo(articleURL)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
sents = sent_tokenize(text)
print(sents)
word_sent = word_tokenize(text.lower())
word_sent

_stopwords = set(stopwords.words('english') + list(punctuation))
_stopwords
word_sent=[word for word in word_sent if word not in _stopwords]
print(word_sent)

from nltk.probability import FreqDist
freq = FreqDist(word_sent)
freq

from heapq import nlargest
nlargest(10, freq, key=freq.get)

from collections import defaultdict
ranking = defaultdict(int)

for i,sent in enumerate(sents):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]
            
ranking

sents_idx = nlargest(4, ranking, key=ranking.get)
sents_idx

[sents[j] for j in sorted(sents_idx)]


def summarize(text, n):
    sents = sent_tokenize(text)
    
    assert n <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))
    
    word_sent=[word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)
    
    
    ranking = defaultdict(int)
    
    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
             
        
    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]

print (summarize(text,3))