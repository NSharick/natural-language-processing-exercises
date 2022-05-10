## Data Preparation Functions - NLP ##

#Imports
import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd

#basic cleaning function
def basic_clean(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    return text

#tokenization function
def tokenize(text):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    return text

#stemming function
def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    text = ' '.join(stems)
    return text

#lemmitization function
def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text = ' '.join(lemmas)
    return text

