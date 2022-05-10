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
    '''
    This function takes in textual data, changes all casing to lower case, normalizes the data
    and removes any characters that are not a-z, 0-9, ' , or a whitespace and returns the cleaned data
    '''
    #change all casing to lower case
    text = text.lower()
    #normalize the data
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    #remove any characters that are not a-z, 0-9, ', or white space using regex
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    #return the cleaned data
    return text

#tokenization function
def tokenize(text):
    '''
    This function takes in textual data and tokenizes it by creating a white space character between 
    every 'word' including splitting words with a ' by placing a whitespace on each side of the character
    '''
    #create the tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    #use the object to tokenize the textual data
    text = tokenizer.tokenize(text, return_str=True)
    #return the tokenized data
    return text

#stemming function
def stem(text):
    '''
    This function stemms the textual data by splitting the data on all white spaces and then converting 
    each word to it's base form. Since it is the words base form it may not always be lexicographically correct.
    '''
    #create the stemming object
    ps = nltk.porter.PorterStemmer()
    #split the data on the whitespaces and use the stemming object to convert the data
    stems = [ps.stem(word) for word in text.split()]
    #change the resulting data from a list of stems back into one large string
    text = ' '.join(stems)
    #return the stemmed textual data
    return text

#lemmitization function
def lemmatize(text):
    '''
    This function lemmatizes textual data by splitting the data on all whitespaces and then converting all 
    words to their root word form. Since it is the root word form it will be lexicographically correct.
    '''
    #Create the lemmatizing object
    wnl = nltk.stem.WordNetLemmatizer()
    #Split the data on whitespaces and lemmatize the words using the created object
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    #change the resulting data from a list of root words back to one large string
    text = ' '.join(lemmas)
    #return the lemmatized textual data
    return text

#removing stopwords function
def remove_stopwords(text, extra_words= [], exclude_words= []):
    '''
    This function creates a stopword list and then removes the words on the list from the textual data 
    that was passed to the function. This functio also includes optional entries for extra words to 
    add to the list and words to exclude from the list
    '''
    #create the stopword list
    stopword_list = stopwords.words('english')
    #remove exclude words from the list if entered
    stopword_list = set(stopword_list) - set(exclude_words)
    #add extra words to the list if entered
    stopword_list = stopword_list.union(set(extra_words))
    #split the words on whitespaces
    words = text.split()
    #remove stopwords from the list using a list comprehension
    filtered_words = [w for w in words if w not in stopword_list]
    #rejoin the split word list into one string
    text_without_stopwords = ' '.join(filtered_words)
    #return the textual data with stopwords removed
    return text_without_stopwords
    