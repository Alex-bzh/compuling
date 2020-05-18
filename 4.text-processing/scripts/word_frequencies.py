#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""List of word frequencies in a text"""

import nltk, unicodedata, string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def text_to_words(path):
    """Splits a text into words.

    Keyword argument:
    path -- path to a file to parse
    """

    with open(path) as file:
        text = file.read()

    tokenizer = RegexpTokenizer("\w+")
    words = tokenizer.tokenize(text)

    return words

def remove_accent_mark(word):
    """Removes the accent marks on a character.
    
    Argument keyword:
    word -- the word to analyse
    """
    word_norm = ""
    for character in word:
        char_norm = unicodedata.normalize('NFKD', character)
        word_norm += char_norm[0]
    return word_norm

def get_occurrences(words):
    """Builds up a dictionary of words and the count of their
    occurrences.
    
    Keyword argument:
    words -- list of tokens
    """
    fr_stopwords = stopwords.words('french')
    [fr_stopwords.append(s.capitalize()) for s in stopwords.words('french')]

    result = {}
    for word in words:
        if word not in fr_stopwords + list(string.punctuation):
            result.update({
                word: result.get(word, 0) + 1
            })
    return result

def sorted_fr(iterable):
    """Sorts a dictionary of occurrences in the format {'word': nb}
    where nb is an integer.
    
    Keyword argument:
    iterable -- a dictionary to sort
    """
    result = list(iterable.items())
    result = sorted(result, key=lambda this:remove_accent_mark(this[0].lower()))
    result = sorted(result, key=lambda this:this[1], reverse=True)
    return result

def main():
    """Triggers the gathering of word frequencies."""

    words = text_to_words('../data/dormeur-du-val.txt')
    occurrences = get_occurrences(words)
    words_sorted = sorted_fr(occurrences)

    print(words_sorted)

if __name__ == "__main__":
    main()