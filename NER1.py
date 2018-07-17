#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:15:59 2018

@author: mayur
"""

 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:24:59 2018

@author: mayur
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import urllib.parse

## initial consts
BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'
TEXT = 'Wayne Rooney'

CONFIDENCE = '0.5'
SUPPORT = '120'
REQUEST = BASE_URL.format(
    text=urllib.parse.quote_plus(TEXT), 
    confidence=CONFIDENCE, 
    support=SUPPORT
)
HEADERS = {'Accept': 'application/json'}
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
all_urls = []

r = requests.get(url=REQUEST, headers=HEADERS)
response = r.json()
resources = response['Resources']

for res in resources:
    all_urls.append(res['@URI'])

values = '(<{0}>)'.format('>) (<'.join(all_urls))

sparql.setQuery(
    """PREFIX vrank:<http://purl.org/voc/vrank#>
       SELECT DISTINCT ?l ?rank
       FROM <http://dbpedia.org> 
       FROM <http://people.aifb.kit.edu/ath/#DBpedia_PageRank>
       WHERE {
           VALUES (?s) {""" + values + 
    """    }
       ?s rdf:type ?p .
       ?p rdfs:label ?l.
       FILTER (lang(?l) = 'en')
} 
    """)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print('resource ---- ', result['l']['value'])