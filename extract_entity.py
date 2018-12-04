# -*- coding: utf-8 -*-
article = '''
Small businesses are certainly not few and far between. According to the U.S. Small Business Administration, there are 29.6 million of them operating across the country. If you're interested in successfully joining their ranks, the last thing you want to do is start a business in an industry with a gloomy outlook. Here are five industries with promising futures, based on data from the U.S. Bureau of Labor Statistics, market research firm IBISWorld and financial information company Sageworks.

As the 75 million baby boomers age, there's increased demand for health care services. According to an outlook by the Bureau of Labor Statistics, more than half of the 20 occupations projected to have the highest percent increase in employment by 2024 are in the health industry. Meeting the needs of an aging population creates opportunities for physical therapists, doctors, optometrists and other specialists to open their own practices.
'''

import spacy
from spacy import displacy
article = article.decode('utf8')
spacy_nlp = spacy.load('en')
document = spacy_nlp(article)

arr_sentence = []
for sentence in document.sents:
    arr_sentence.append(sentence.text)

for sentence in arr_sentence:
    sentence = spacy_nlp(sentence)
    quantifier = ''
    adjective = ''
    noun = ''
    for ents_token in sentence.ents:
      if ents_token.label_ == 'CARDINAL' or ents_token.label_ == 'PERCENT':
        quantifier += str(ents_token)
    for token in sentence:
      print(token.tag_, token.pos_, token.text)
      if str(token.pos_) == 'ADJ':
        adjective += token.text + ','
      if str(token.pos_) == 'NOUN':
        noun += token.text + ','
      
    print(sentence)
    print(adjective)
    print(noun)
    print(quantifier)
    