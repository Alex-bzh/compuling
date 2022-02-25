#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   Modules to import
#
import urllib.request
from bs4 import BeautifulSoup

def get_html_from_url(url, charset='utf-8'):
    """Extracts the HTML code from a single URL.

    Keyword arguments:
    url -- the url to scrap
    charset -- the charset used to decode caracters (default utf-8)
    """
    headers = { 'User-agent' : 'HTML extractor (Alexandre Roulois)' }
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as fichier:
        html = fichier.read().decode(charset)
    return html

def parse_html_by_class(html, selector):
    """Extracts tags from HTML whith CSS selector.
    
    Keyword arguments:
    html -- the html page
    selector -- the CSS selector
    """
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select(selector)
    return tags