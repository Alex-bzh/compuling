#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

def get_HTML_from_URL(url):
    """
        Extract the HTML code from a single URL.
    """
    headers = { 'User-agent' : 'HTML extractor (Alexandre Roulois)' }
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as fichier:
        html = fichier.read().decode('utf-8')
    return html

def parse_HTML_by_class(html, selector):
    """
        Extrait des balises d’une page HTML grâce à un sélecteur CSS.
    """
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select(selector)
    return tags