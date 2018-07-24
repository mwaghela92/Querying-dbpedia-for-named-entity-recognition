# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:49:23 2018

@author: mayur
"""

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
Text = """

Mr. Speaker, Mr. President, and distinguished Members of the House and Senate, honored guests, and fellow citizens:
Less than 3 weeks ago, I joined you on the West Front of this very building and, looking over the monuments to our proud past, offered you my hand in filling the next page of American history with a story of extended prosperity and continued peace. And tonight I'm back to offer you my plans as well. The hand remains extended; the sleeves are rolled up; America is waiting; and now we must produce. Together, we can build a better America.
It is comforting to return to this historic Chamber. Here, 22 years ago, I first raised my hand to be sworn into public life. So, tonight I feel as if I'm returning home to friends. And I intend, in the months and years to come, to give you what friends deserve: frankness, respect, and my best judgment about ways to improve America's future. In return, I ask for an honest commitment to our common mission of progress. If we seize the opportunities on the road before us, there'll be praise enough for all. The people didn't send us here to bicker, and it's time to govern.
And many Presidents have come to this Chamber in times of great crisis: war and depression, loss of national spirit. And 8 years ago, I sat in that very chair as President Reagan spoke of punishing inflation and devastatingly high interest rates and people out of work — American confidence on the wane. And our challenge is different. We're fortunate — a much changed landscape lies before us tonight. So, I don't propose to reverse direction. We're headed the right way, but we cannot rest. We're a people whose energy and drive have fueled our rise to greatness. And we're a forward-looking nation — generous, yes, but ambitious, not for ourselves but for the world. Complacency is not in our character — not before, not now, not ever.
And so, tonight we must take a strong America and make it even better. We must address some very real problems. We must establish some very clear priorities. And we must make a very substantial cut in the Federal budget deficit. Some people find that agenda impossible, but I'm presenting to you tonight a realistic plan for tackling it. My plan has four broad features: attention to urgent priorities, investment in the future, an attack on the deficit, and no new taxes. This budget represents my best judgment of how we can address our priorities. There are many areas in which we would all like to spend more than I propose; I understand that. But we cannot until we get our fiscal house in order.
Next year alone, thanks to economic growth, without any change in the law, the Federal Government will take in over $80 billion more than it does this year. That's right — over $80 billion in new revenues, with no increases in taxes. And our job is to allocate those new resources wisely. We can afford to increase spending by a modest amount, but enough to invest in key priorities and still cut the deficit by almost 40 percent in 1 year. And that will allow us to meet the targets set forth in the Gramm-Rudman-Hollings law. But to do that, we must recognize that growth above inflation in Federal programs is not preordained, that not all spending initiatives were designed to be immortal.
I make this pledge tonight: My team and I are ready to work with the Congress, to form a special leadership group, to negotiate in good faith, to work day and night — if that's what it takes — to meet the budget targets and to produce a budget on time.
We cannot settle for business as usual. Government by continuing resolution, or government by crisis, will not do. And I ask the Congress tonight to approve several measures which will make budgeting more sensible. We could save time and improve efficiency by enacting 2-year budgets. Forty-three Governors have the line-item veto. Presidents should have it, too. And at the very least, when a President proposes to rescind Federal spending, the Congress should be required to vote on that proposal instead of killing it by inaction. And I ask the Congress to honor the public's wishes by passing a constitutional amendment to require a balanced budget. Such an amendment, once phased in, will discipline both the Congress and the executive branch.
Several principles describe the kind of America I hope to build with your help in the years ahead. We will not have the luxury of taking the easy, spendthrift approach to solving problems because higher spending and higher taxes put economic growth at risk. Economic growth provides jobs and hope. Economic growth enables us to pay for social programs. Economic growth enhances the security of the Nation, and low tax rates create economic growth.
I believe in giving Americans greater freedom and greater choice. And I will work for choice for American families, whether in the housing in which they live, the schools to which they send their children, or the child care they select for their young. You see, I believe that we have an obligation to those in need, but that government should not be the provider of first resort for things that the private sector can produce better. I believe in a society that is free from discrimination and bigotry of any kind. And I will work to knock down the barriers left by past discrimination and to build a more tolerant society that will stop such barriers from ever being built again.
I believe that family and faith represent the moral compass of the Nation. And I'll work to make them strong, for as Benjamin Franklin said: ``If a sparrow cannot fall to the ground without His notice, can a great nation rise without His aid? And I believe in giving people the power to make their own lives better through growth and opportunity. And together, let's put power in the hands of people.
Three weeks ago, we celebrated the bicentennial inaugural, the 200th anniversary of the first Presidency. And if you look back, one thing is so striking about the way the Founding Fathers looked at America. They didn't talk about themselves. They talked about posterity. They talked about the future. And we, too, must think in terms bigger than ourselves. We must take actions today that will ensure a better tomorrow. We must extend American leadership in technology, increase long-term investment, improve our educational system, and boost productivity. These are the keys to building a better future, and here are some of my recommendations:
I propose almost $2.2 billion for the National Science Foundation to promote basic research and keep us on track to double its budget by 1993.
I propose to make permanent the tax credit for research and development.
I've asked Vice President Quayle to chair a new Task Force on Competitiveness.
And I request funding for NASA [National Aeronautics and Space Administration] and a strong space program, an increase of almost $2.4 billion over the current fiscal year. We must have a manned space station; a vigorous, safe space shuttle program; and more commercial development in space. The space program should always go ``full throttle up. And that's not just our ambition; it's our destiny.
I propose that we cut the maximum tax rate on capital gains to increase long-term investment. History on this is clear — this will increase revenues, help savings, and create new jobs. We won't be competitive if we leave whole sectors of America behind. This is the year we should finally enact urban enterprise zones and bring hope to the inner cities.
But the most important competitiveness program of all is one which improves education in America. When some of our students actually have trouble locating America on a map of the world, it is time for us to map a new approach to education. We must reward excellence and cut through bureaucracy. We must help schools that need help the most. We must give choice to parents, students, teachers, and principals; and we must hold all concerned accountable. In education, we cannot tolerate mediocrity. I want to cut that dropout rate and make America a more literate nation, because what it really comes down to is this: The longer our graduation lines are today, the shorter our unemployment lines will be tomorrow.
So, tonight I'm proposing the following initiatives: the beginning of a $500 million program to reward America's best schools, merit schools; the creation of special Presidential awards for the best teachers in every State, because excellence should be rewarded; the establishment of a new program of National Science Scholars, one each year for every Member of the House and Senate, to give this generation of students a special incentive to excel in science and mathematics; the expanded use of magnet schools, which give families and students greater choice; and a new program to encourage alternative certification, which will let talented people from all fields teach in our classrooms. I've said I'd like to be the ``Education President. And tonight, I'd ask you to join me by becoming the ``Education Congress.
Just last week, as I settled into this new office, I received a letter from a mother in Pennsylvania who had been struck by my message in the Inaugural Address. ``Not 12 hours before, she wrote, ``my husband and I received word that our son was addicted to cocaine. He had the world at his feet. Bright, gifted, personable — he could have done anything with his life. And now he has chosen cocaine. ``And please, she wrote, ``find a way to curb the supply of cocaine. Get tough with the pushers. Our son needs your help.
My friends, that voice crying out for help could be the voice of your own neighbor, your own friend, your own son. Over 23 million Americans used illegal drugs last year, at a staggering cost to our nation's well-being. Let this be recorded as the time when America rose up and said no to drugs. The scourge of drugs must be stopped. And I am asking tonight for an increase of almost a billion dollars in budget outlays to escalate the war against drugs. The war must be waged on all fronts. Our new drug czar, Bill Bennett, and I will be shoulder to shoulder in the executive branch leading the charge.
Some money will be used to expand treatment to the poor and to young mothers. This will offer the helping hand to the many innocent victims of drugs, like the thousands of babies born addicted or with AIDS because of the mother's addiction. Some will be used to cut the waiting time for treatment. Some money will be devoted to those urban schools where the emergency is now the worst. And much of it will be used to protect our borders, with help from the Coast Guard and the Customs Service, the Departments of State and Justice, and, yes, the U.S. military.
I mean to get tough on the drug criminals. And let me be clear: This President will back up those who put their lives on the line every single day — our local police officers. My budget asks for beefed-up prosecution, for a new attack on organized crime, and for enforcement of tough sentences — and for the worst kingpins, that means the death penalty. I also want to make sure that when a drug dealer is convicted there's a cell waiting for him. And he should not go free because prisons are too full. And so, let the word go out: If you're caught and convicted, you will do time.
But for all we do in law enforcement, in interdiction and treatment, we will never win this war on drugs unless we stop the demand for drugs. So, some of this increase will be used to educate the young about the dangers of drugs. We must involve the parents. We must involve the teachers. We must involve the communities. And, my friends, we must involve ourselves, each and every one of us in this concern.
One problem related to drug use demands our urgent attention and our continuing compassion, and that is the terrible tragedy of AIDS. I'm asking for $1.6 billion for education to prevent the disease and for research to find a cure.
If we're to protect our future, we need a new attitude about the environment. We must protect the air we breathe. I will send to you shortly legislation for a new, more effective Clean Air Act. It will include a plan to reduce by date certain the emissions which cause acid rain, because the time for study alone has passed, and the time for action is now. We must make use of clean coal. My budget contains full funding, on schedule, for the clean coal technology agreement that we've made with Canada. We've made that agreement with Canada, and we intend to honor that agreement. We must not neglect our parks. So, I'm asking to fund new acquisitions under the Land and Water Conservation Fund. We must protect our oceans. And I support new penalties against those who would dump medical waste and other trash into our oceans. The age of the needle on the beaches must end.
And in some cases, the gulfs and oceans off our shores hold the promise of oil and gas reserves which can make our nation more secure and less dependent on foreign oil. And when those with the most promise can be tapped safely, as with much of the Alaska National Wildlife Refuge, we should proceed. But we must use caution; we must respect the environment. And so, tonight I'm calling for the indefinite postponement of three lease sales which have raised troubling questions, two off the coast of California and one which could threaten the Everglades in Florida. Action on these three lease sales will await the conclusion of a special task force set up to measure the potential for environmental damage.
I'm directing the Attorney General and the Administrator of the Environmental Protection Agency to use every tool at their disposal to speed and toughen the enforcement of our laws against toxic-waste dumpers. I want faster cleanups and tougher enforcement of penalties against polluters.
In addition to caring for our future, we must care for those around us. A decent society shows compassion for the young, the elderly, the vulnerable, and the poor. Our first obligation is to the most vulnerable — infants, poor mothers, children living in poverty — and my proposed budget recognizes this. I ask for full funding of Medicaid, an increase of over $3 billion, and an expansion of the program to include coverage of pregnant women who are near the poverty line. I believe we should help working families cope with the burden of child care. Our help should be aimed at those who need it most: low-income families with young children. I support a new child care tax credit that will aim our efforts at exactly those families, without discriminating against mothers who choose to stay at home.
Now, I know there are competing proposals. But remember this: The overwhelming majority of all preschool child care is now provided by relatives and neighbors and churches and community groups. Families who choose these options should remain eligible for help. Parents should have choice. And for those children who are unwanted or abused or whose parents are deceased, we should encourage adoption. I propose to reenact the tax deduction for adoption expenses and to double it to $3,000. Let's make it easier for these kids to have parents who love them.
We have a moral contract with our senior citizens. And in this budget, Social Security is fully funded, including a full cost-of-living adjustment. We must honor our contract.
We must care about those in the shadow of life, and I, like many Americans, am deeply troubled by the plight of the homeless. The causes of homelessness are many; the history is long. But the moral imperative to act is clear. Thanks to the deep well of generosity in this great land, many organizations already contribute, but we in government cannot stand on the sidelines. In my budget, I ask for greater support for emergency food and shelter, for health services and measures to prevent substance abuse, and for clinics for the mentally ill. And I propose a new initiative involving the full range of government agencies. We must confront this national shame.
There's another issue that I've decided to mention here tonight. I've long believed that the people of Puerto Rico should have the right to determine their own political future. Personally, I strongly favor statehood. But I urge the Congress to take the necessary steps to allow the people to decide in a referendum.
Certain problems, the result of decades of unwise practices, threaten the health and security of our people. Left unattended, they will only get worse. But we can act now to put them behind us.
Earlier this week, I announced my support for a plan to restore the financial and moral integrity of our savings system. I ask Congress to enact our reform proposals within 45 days. We must not let this situation fester. We owe it to the savers in this country to solve this problem. Certainly, the savings of Americans must remain secure. Let me be clear: Insured depositors will continue to be fully protected, but any plan to refinance the system must be accompanied by major reform. Our proposals will prevent such a crisis from recurring. The best answer is to make sure that a mess like this will never happen again. The majority of thrifts in communities across the Nation have been honest. They've played a major role in helping families achieve the dream of home ownership. But make no mistake, those who are corrupt, those who break the law, must be kicked out of the business; and they should go to jail.
We face a massive task in cleaning up the waste left from decades of environmental neglect at America's nuclear weapons plants. Clearly, we must modernize these plants and operate them safely. That's not at issue; our national security depends on it. But beyond that, we must clean up the old mess that's been left behind. And I propose in this budget to more than double our current effort to do so. This will allow us to identify the exact nature of the various problems so we can clean them up, and clean them up we will.
We've been fortunate during these past 8 years. America is a stronger nation than it was in 1980. Morale in our Armed Forces has been restored; our resolve has been shown. Our readiness has been improved, and we are at peace. There can no longer be any doubt that peace has been made more secure through strength. And when America is stronger, the world is safer.
Most people don't realize that after the successful restoration of our strength, the Pentagon budget has actually been reduced in real terms for each of the last 4 years. We cannot tolerate continued real reduction in defense. In light of the compelling need to reduce the deficit, however, I support a 1-year freeze in the military budget, something I proposed last fall in my flexible freeze plan. And this freeze will apply for only 1 year, and after that, increases above inflation will be required. I will not sacrifice American preparedness, and I will not compromise American strength.
I should be clear on the conditions attached to my recommendation for the coming year: The savings must be allocated to those priorities for investing in our future that I've spoken about tonight. This defense freeze must be a part of a comprehensive budget agreement which meets the targets spelled out in Gramm-Rudman-Hollings law without raising taxes and which incorporates reforms in the budget process.
I've directed the National Security Council to review our national security and defense policies and report back to me within 90 days to ensure that our capabilities and resources meet our commitments and strategies. I'm also charging the Department of Defense with the task of developing a plan to improve the defense procurement process and management of the Pentagon, one which will fully implement the Packard commission report. Many of these changes can only be made with the participation of the Congress, and so, I ask for your help. We need fewer regulations. We need less bureaucracy. We need multiyear procurement and 2-year budgeting. And frankly — and don't take this wrong — we need less congressional micromanagement of our nation's military policy. I detect a slight division on that question, but nevertheless.
Securing a more peaceful world is perhaps the most important priority I'd like to address tonight. You know, we meet at a time of extraordinary hope. Never before in this century have our values of freedom, democracy, and economic opportunity been such a powerful and intellectual force around the globe. Never before has our leadership been so crucial, because while America has its eyes on the future, the world has its eyes on America.
And it's a time of great change in the world, and especially in the Soviet Union. Prudence and common sense dictate that we try to understand the full meaning of the change going on there, review our policies, and then proceed with caution. But I've personally assured General Secretary Gorbachev that at the conclusion of such a review we will be ready to move forward. We will not miss any opportunity to work for peace. The fundamental facts remain that the Soviets retain a very powerful military machine in the service of objectives which are still too often in conflict with ours. So, let us take the new openness seriously, but let's also be realistic. And let's always be strong.
There are some pressing issues we must address. I will vigorously pursue the Strategic Defense Initiative. The spread, and even use, of sophisticated weaponry threatens global security as never before. Chemical weapons must be banned from the face of the Earth, never to be used again. And look, this won't be easy. Verification — extraordinarily difficult, but civilization and human decency demand that we try. And the spread of nuclear weapons must be stopped. And I'll work to strengthen the hand of the International Atomic Energy Agency. Our diplomacy must work every day against the proliferation of nuclear weapons.
And around the globe, we must continue to be freedom's best friend. And we must stand firm for self-determination and democracy in Central America, including in Nicaragua. It is my strongly held conviction that when people are given the chance they inevitably will choose a free press, freedom of worship, and certifiably free and fair elections.
We must strengthen the alliance of the industrial democracies, as solid a force for peace as the world has ever known. And this is an alliance forged by the power of our ideals, not the pettiness of our differences. So, let's lift our sights to rise above fighting about beef hormones, to building a better future, to move from protectionism to progress.
I've asked the Secretary of State to visit Europe next week and to consult with our allies on the wide range of challenges and opportunities we face together, including East-West relations. And I look forward to meeting with our NATO partners in the near future.
And I, too, shall begin a trip shortly to the far reaches of the Pacific Basin, where the winds of democracy are creating new hope and the power of free markets is unleashing a new force. When I served as our representative in China 14 or 15 years ago, few would have predicted the scope of the changes we've witnessed since then. But in preparing for this trip, I was struck by something I came across from a Chinese writer. He was speaking of his country, decades ago, but his words speak to each of us in America tonight. ``Today, he said, ``we're afraid of the simple words like `goodness' and `mercy' and `kindness.' My friends, if we're to succeed as a nation, we must rediscover those words.
In just 3 days, we mark the birthday of Abraham Lincoln, the man who saved our Union and gave new meaning to the word ``opportunity. Lincoln once said: ``I hold that while man exists, it is his duty to improve not only his own condition but to assist in ameliorating that of mankind. It is this broader mission to which I call all Americans, because the definition of a successful life must include serving others.
And to the young people of America, who sometimes feel left out, I ask you tonight to give us the benefit of your talent and energy through a new program called YES, for Youth Entering Service to America.
To those men and women in business, remember the ultimate end of your work: to make a better product, to create better lives. I ask you to plan for the longer term and avoid that temptation of quick and easy paper profits.
To the brave men and women who wear the uniform of the United States of America, thank you. Your calling is a high one: to be the defenders of freedom and the guarantors of liberty. And I want you to know that this nation is grateful for your service.
To the farmers of America, we appreci

"""
len_text = len(Text)
all_keywords = list()


for i in range(0,len_text,5000):
    TEXT = Text[i:i+5010]

    CONFIDENCE = '0.7'
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

print(len(all_keywords))
print(len(unique_keywords))
   