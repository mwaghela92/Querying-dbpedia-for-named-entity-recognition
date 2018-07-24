# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:51:56 2018

@author: mayur
"""


from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import urllib.parse
from nltk.corpus import stopwords

## initial consts
BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'

###... The actual text from which we want to mine the key words
TEXT = """There are many important booklets at The Library of Senate.
I saw Titanic movie first time in cinema hall.
I saw the Eiffel Tower in scenery only.
'To Kill a Mockingbird' was my favorite book in high school.
I drive an old Toyota. It’s not a luxurious car, but it works.

"""

CONFIDENCE = '0.2'
SUPPORT = '50'

###... Below three lines can be used to remove stop words and then join again
###... to form a string for processing urls

#Text = Text.split()
#Text1 = [word for word in Text if word not in stopwords.words('english')]
#TEXT = ' '.join(Text1)

###... REQUEST is prepping the above text to be sent as an search url. Increasing
###... confidence decreases the number of key words extracted, less confidence gives
###... noisy or unwanted keywords

REQUEST = BASE_URL.format(
    text=urllib.parse.quote_plus(TEXT), 
    confidence=CONFIDENCE, 
    support=SUPPORT
)
HEADERS = {'Accept': 'application/json'}
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

###... All the urls which are to be used for mining data from DBpedia are stored
###... in the all_urls

all_urls = []
r = requests.get(url = REQUEST , headers=HEADERS)
response = r.json()
resources = response['Resources']

###... storing all the urls in resources in all_urls and then formatting them 
###... into a string named 'values' to be passed into the sparql query

for res in resources:
    all_urls.append(res['@URI'])

all_keywords = list()
    
values = '(<{0}>)'.format('>) (<'.join(all_urls))

sparql.setQuery(
    """PREFIX vrank:<http://purl.org/voc/vrank#>
       SELECT DISTINCT ?l ?rank ?sname
       FROM <http://dbpedia.org> 
       FROM <http://people.aifb.kit.edu/ath/#DBpedia_PageRank>
       WHERE {
           VALUES (?s) {""" + values + 
    """    }
       ?s rdf:type ?p .
       ?p rdfs:label ?l.
        ?s dct:subject ?sub .
           ?sub rdfs:label ?sname.
       FILTER (lang(?l) = 'en')
    } order by ?rank
           limit 3
        """)

###... The above sparql query extracts the following details:
###... ?s gives resource of the url,
###... ?p is type/ontology of resource ?s
###... ?l is the label of the ontology class of ?p
###... ?sub gives the subject of the resource and ?sname its label 
###... Thus, in all, we extract the labels of ontology classes and its subjects


sparql.setReturnFormat(JSON)
results = sparql.query().convert()
    

for result in results["results"]["bindings"]:
    all_keywords.append( result['l']['value'])
    
for result in results["results"]["bindings"]:
    all_keywords.append( result['sname']['value'])
    
#print (y)
#print(x)
        
#item = list()
for res in resources:
    all_keywords.append(res['@surfaceForm'])
    
unique_keywords = set(all_keywords)
print(unique_keywords)

   