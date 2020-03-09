#!/usr/bin/env python
#-*- coding: utf-8 -*-

import nltk, string
from nltk.corpus import gutenberg, stopwords

def occurrences(words):
    """Builds up a dictionary of words and the count of their
    occurrences. Ex : {'boat': 34, 'whale': 55}
    
    Keyword argument:
    words -- list of tokens
    """
    result = {}
    for word in words:
        if word not in stopwords.words('english') + list(string.punctuation):
            result.update({
                word: result.get(word, 0) + 1
            })
    return result

# List of words in Moby Dick
words = gutenberg.words('melville-moby_dick.txt')

# Builds up a dictionary of occurrences
occurrences = occurrences(words)

# Transforms the dict into a sortable object
results = list(occurrences.items())

# Lowercase before sorting
results.sort(key=lambda this:this[0].lower())

# Sorting by decreasing number of occurrences
results.sort(key=lambda this:this[1], reverse=True)