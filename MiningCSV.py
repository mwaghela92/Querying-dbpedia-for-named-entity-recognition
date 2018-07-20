# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:25:21 2018

@author: mayur
"""

import pandas as pd

df = pd.read_csv('E:\mayur\dbpedia\Querying-dbpedia-for-named-entity-recognition\Data\Topic Mining Trial.csv')
BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'
CONFIDENCE = '0.5'
SUPPORT = '50'
#df['flag']
y = list()
for i in range(len(df)):
    #i=0
    Text = df.loc[i]['Article']
    
    
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
    print (1)
    response = r.json()
    resources = response['Resources']
    print (2)
    for res in resources:
        all_urls.append(res['@URI'])
    
    x = list()
    
    for i in range(len(all_urls)):
        #i=0
        
        values = '(<{0}>)'.format(all_urls[i])
        
        
       # values = '(<{0}>)'.format('>) (<'.join(all_urls))
    
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
    x = list()
    for i in mainlist:
        if mainlist[i][:]:
            print(i,':', mainlist[i][:])
            print('\n')
            x.append(i)
    y.append([x])
            #x = ' '.join(x)
    
    #df['Tags'] = x
    
df['Tags']= y
        
    