#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   Modules to import
#
import nltk
import nltk.data
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

def main():

    # Tokenizer configuration
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

    # Lemmatizer instance
    lemmatizer = WordNetLemmatizer()

    txt = "The/at sun/nn did/vbd not/* shine/vbi ./. It/pps was/vbd too/ql wet/aj to/to play/vbi ./."

    sents = sent_tokenize(txt)

    for sent in sents:
        for tagged_word in sent.split():
            word, tag = tagged_word.split('/')
            tag = tag[0]
            if tag in 'ranv':
                lemma = lemmatizer.lemmatize(word, pos=tag)
                synsets = wordnet.synsets(lemma, pos=tag)
                translations = set()
                for synset in synsets:
                    for translation in synset.lemma_names('fra'):
                        translations.add(translation)
                if translations:
                    guessed = list(translations)[0]
                    print(word, '=>', guessed)

if __name__ == '__main__':
    main()