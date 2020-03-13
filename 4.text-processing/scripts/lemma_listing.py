#!/usr/bin/env python
#-*- coding: utf-8 -*-

import nltk
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def main():

    tokenizer = RegexpTokenizer('\w+')
    lemmatizer = WordNetLemmatizer()
    text = "The sun did not shine. It was too wet to play."
    sents = sent_tokenize(text)
    for sent in sents:
        words = tokenizer.tokenize(sent)
        for word in words:
            if word not in stopwords.words('english'):
                lemma = lemmatizer.lemmatize(word)
                print(word, '=>', lemma)

if __name__ == '__main__':
    main()