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
from nltk.corpus import stopwords
import pandas as pd
entities = pd.DataFrame({'Entities' : ['Count'] , 'person' : [0],'place' : [0],
                                   'animal' : [0],'city' : [0], 'country' : [0],
                                   'organisation' : [0],'Food' : [0]})

## initial consts
BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'
Text = 
CONFIDENCE = '0.2'
SUPPORT = '10'

    Text = 
    Text = Text.split()
    Text1 = [word for word in Text if word not in stopwords.words('english')]
    TEXT = ' '.join(Text1)
    REQUEST = BASE_URL.format(
        text=urllib.parse.quote_plus(TEXT), 
        confidence=CONFIDENCE, 
        support=SUPPORT
    )
    HEADERS = {'Accept': 'application/json'}
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    all_urls = []
    
    r = requests.get(url = REQUEST , headers=HEADERS)
    response = r.json()
    resources = response['Resources']
    
    for res in resources:
        all_urls.append(res['@URI'])
    
    x = list()
        
        for i in range(len(all_urls)):
            #i=0
            
            values = '(<{0}>)'.format(all_urls[i])
        
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
            } limit 6
                """)
        
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            
            x.append([])
            for result in results["results"]["bindings"]:
                x[i].append( result['l']['value'])
            
            
        item = list()
        for res in resources:
            item.append(res['@surfaceForm'])
        
        mainlist = {}
        j = 0
        for i in item:
            mainlist[i] = x[j]
            j = j +1
        
        for i in mainlist:
            print(i,':', mainlist[i][:])
            print ('\n')
            
        
        #entities.ProperNoun = item
        
        m=0
        
        for i in mainlist:   
            print(i)
            for j in range(1,len(entities.columns)):
                if (entities.columns[j] in mainlist[i][:]):
                        entities.loc[m,entities.columns[j]]= entities.loc[m,entities.columns[j]] +1
