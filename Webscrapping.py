# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:49:23 2018

@author: mayur
"""

from goose import Goose
from requests import get

response = get('http://www.nytimes.com/2015/05/19/health/study-finds-dense-breast-tissue-isnt-always-a-high-cancer-risk.html?src=me&ref=general')
extractor = Goose()
article = extractor.extract(raw_html=response.content)
text = article.cleaned_text