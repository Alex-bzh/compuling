#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   Modules to import
#
import re

def get_metadata(filename):
    """Defines metadata from a filename and pushes them into an array
    
    Keyword argument:
    filename -- the filename to parse
    """
    output = []
    pattern = 'S(?P<season>[0-9]{2})E(?P<episode>[0-9]{2,3})-(?P<title>.+).txt'
    metas = re.match(pattern, filename)
    output.append(metas.group('title'))
    output.append(metas.group('season'))
    output.append(metas.group('episode'))
    return output

def get_alias(sentence):
    """Regex that looks in a sentence for the alias of a transcriber
    
    Keyword argument:
    sentence -- the string in which look for an alias
    """
    if sentence.startswith('Rédigé par'):
        pattern = 'Rédigé par\s?(?P<alias>[A-Za-z1-9]+)\s?.+'
        m = re.match(pattern, sentence)
        return m.group('alias')
    else:
        return ''

def add_meta(what, where, in_which):
    """Adds a metadata at a specific index in an array of metadata
    
    Keyword arguments:
    what -- the object to record
    where -- the index where to record the object
    in_which -- the array of metadata to update
    """
    in_which[where].append(what)