#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib.request

def get_HTML_from_URL(url):
    """
        Extract the HTML code from a single URL.
    """
    headers = { 'User-agent' : 'HTML extractor (Alexandre Roulois)' }
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(url) as fichier:
        html = fichier.read().decode('utf-8')
    return html