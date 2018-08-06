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

'Wayne Rooney plays for Manchester United. He was born in England. He stays in United States. He is a member of FIFA'

'He loved Paris. The france national team won the worldcup 2018 and that was amazing. he travelled by jet airways'

'Obama was born in 1961 in Honolulu, Hawaii, two years after the territory was admitted to the Union as the 50th state. Raised largely in Hawaii, he also spent one year of his childhood in Washington state and four years in Indonesia. After graduating from Columbia University in 1983, he worked as a community organizer in Chicago.'

'The India cricket team are currently touring England between July and September 2018 to play five Tests, three One Day International (ODIs) and three Twenty20 International (T20Is) matches.[1][2][3] India will also play a first-class match against Essex in July at Chelmsford.[4]. In the second T20I match of the tour, MS Dhoni played in his 500th international cricket match.[5] He became the ninth player overall, and the third Indian, to reach the milestone.[6] India went on to win the T20I series 2–1.[7] In the second ODI match, Dhoni became the twelfth batsman, and fourth from India, to score 10,000 runs in ODIs.[8] '
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import urllib.parse
from nltk.corpus import stopwords

## initial consts
BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'
Text = 'Obama born 1961 Honolulu, Hawaii, two years after territory admitted Union 50th state. Raised largely Hawaii, he also spent one year his childhood Washington. four years Indonesia. After graduating Columbia Universty 1983, he worked community organizer Chicago.'
CONFIDENCE = '0.5'
SUPPORT = '10'

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

for i in mainlist:
    print(i,':', mainlist[i][:])
    print ('\n')
    
import pandas as pd
entities = pd.DataFrame(columns = ['ProperNoun','person','place','animal',
                                   'city', 'country','organisation'])
entities.ProperNoun = item

m=0
#i=0
# j =5
for i in mainlist:   
    for j in range(1,len(entities.columns)):
        if (entities.columns[j] in mainlist[i][:]):
                entities.loc[m,entities.columns[j]]= 'True'
        else:
            print('none')
    m= +1
                
    
    
    
