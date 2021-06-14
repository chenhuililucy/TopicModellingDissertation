import operator 

"""
Backtesting the performance dictionary 
"""


# ''' 

# The first part of this piece of code 


# ##########################################################################################################################################

               # Data Dependencies: 

                 #  CSV FILES #

# postperf.csv -------- csv with all positive performance ngrams 
# negperf.csv -------- csv with all negative performance ngrams  
# amplifier.csv  -------- csv with all amplifiers ngrams  
# negator.csv --------csv with all negators ngrams  
# bad.csv ------ csv with all words of which, when appended to performance words, result in a negative performance

                  #  CORPUS  #

# Corpus where all MD&A files are stored


# ##########################################################################################################################################


"""
Output file: sentence.csv 
# Want: for each sentence of of dictionary, write the no. of sentence in the doc 
# For each no. of sentence, output field write posperf,negperf,internal,external 
filename-------- write filename for every first sentence of the file, for the following sentences after the first, shows "none" 
sentnolist-------- outputs the no. of the sentence in the file 
posperfsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in posperflist.csv
negperfsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in negperflist.csv
internalsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in int.csv
externalsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in ext.csv
"""


###################### PLEASE MODIFY THE FOLLOWING DIRECTORIES#####################

######################        YOUR INPUT FILES            #####################
import re 
import glob
import os
import csv
import nltk 
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams
#nltk.download('punkt')

###################### PLEASE MODIFY THE FOLLOWING DIRECTORIES#####################

######################        YOUR INPUT FILES            #####################

#Change your directory to one which contains all files
#os.chdir("/Users/lucy/Desktop/assortedcodes/builddic")

#The corpus is the main folder that contains all your MD&A files 
corpus="/Users/lichenhuilucy/Desktop/newdic/*.txt"
negator="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negatorfinal.csv"
amplifier="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/amplifiedfinal.csv"
negative="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negativelemma.csv"
positive="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/positivelemma.csv"
bad="//Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/bad.csv"
good="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/good.csv"


######################        YOUR OUTPUT FILES            #####################

#csv1 outputs metrics per sentence
csv1="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/name5.csv"
#csv2 outputs metrics per document
csv2="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/name3.csv"
#Output file with all sentence matches
direct="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/examplesentences0.txt"

#####################################################################################

posperdict=defaultdict(list)
negperfdict=defaultdict(list)
amplifierset=set()
negatorset=set()
badset=set()
goodset=set()

o=[]
p=[]

DEBUG=False

posperflist=[]

with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMpositive.csv","r") as posfile: 
#with open("posperflist.csv","r") as posfile: 
    poswords=csv.reader(posfile)
    for row in poswords: 
        singleposperword=row[0].lower()
        posperflist.append(singleposperword)
        #print(internalwordlist)

posperflist=set(posperflist)
#load in negative performance word list 

negperflist=[]
with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMnegative.csv","r") as negfile: 
#with open("negaperflist.csv","r") as negfile
    negwords=csv.reader(negfile)
    for row in negwords: 
        singlenegperfword=row[0].lower()
        negperflist.append(singlenegperfword)
        #print(internalwordlist)
negperflist=set(negperflist)


def combine2(): 
    o=[]
    p=[]
    amplifier="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/amplifiedfinal.csv"
    negative="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negativelemma.csv"
    positive="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/positivelemma.csv"
    os.chdir("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001")
    posperflist=[]
    with open(positive,"r") as posfile: 
        records=csv.reader(posfile)
        for row in records:
            posperf=row[0].lower()
            if len(posperf.split(" "))>1: 
                w1=posperf.split(" ")[0]
                w2=posperf.split(" ")[1]
            else: 
                w1=posperf
                w2="."
            
            posperdict[w1].append(w2)


    with open(negative,"r") as negfile: 
        records=csv.reader(negfile)
        for row in records:
            negperf=row[0].lower()
            if len(negperf.split(" "))>1: 
                w1=negperf.split(" ")[0]
                w2=negperf.split(" ")[1]
            else: 
                w1=negperf
                w2="."
            
            negperfdict[w1].append(w2)

    with open(bad,"r") as badf: 
        records1=csv.reader(badf)
        for row in records1:
            badf1=row[0].lower()
            badset.add(badf1)


    with open(good,"r") as goodf: 
        records1=csv.reader(goodf)
        for row in records1:
            goodf1=row[0].lower()
            goodset.add(goodf1)


    with open(amplifier,"r") as ampfile: 
        records1=csv.reader(ampfile)
        for row in records1:
            amplifier1=row[0].lower()
            amplifierset.add(amplifier1)
    
    with open(negator,"r") as negfile: 
        records1=csv.reader(negfile)
        for row in records1:
            negator1=row[0].lower()
            negatorset.add(negator1)
                


f1=[]


                   ###################
def searchwords(): 
    
    global sentlist
    combine2()
    posperflist=[]
    

    """
    def c(i,a,b,ww,d,cnt,BOOL): 
        if dict[ww[i+b]] is not None:
            if ww[i+a+b] in d[ww[i+b]]: 
                # print(ww[i:i+a+b+1])
                # print(ww[i])
                # print(ww[i+b])
                # print(ww[i+a+b])
                cnt+=sum([a,b])
                i=i+a+b 
                BOOL=False
                return cnt,BOOL,i
        return None 
    def b(i,a,b,ww,s,cnt,BOOL):
        if fww[i+a+b] in s:
            # print(ww[i:i+a+b+1]) 
            # print(ww[i])
            # print(ww[i+b])
            # print(ww[i+a+b])
            i=i+a+b 
            negperfcnt+=a+b
            BOOl=False
            return cnt, BOOL, i
        return None
    """


    ########

    #LOAD LM 

    with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMpositive.csv","r") as posfile: 
    #with open("posperflist.csv","r") as posfile: 
        poswords=csv.reader(posfile)
        for row in poswords: 
            singleposperword=row[0].lower()
            posperflist.append(singleposperword)
            #print(internalwordlist)

    posperflist=set(posperflist)
    #load in negative performance word list 

    negperflist=[]
    with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMnegative.csv","r") as negfile: 
    #with open("negaperflist.csv","r") as negfile
        negwords=csv.reader(negfile)
        for row in negwords: 
            singlenegperfword=row[0].lower()
            negperflist.append(singlenegperfword)
            #print(internalwordlist)
    negperflist=set(negperflist)


    ########

    from collections import defaultdict


    #def internal wordlist 

    internaldict=defaultdict(list)




    #print(negperfdict)

    def merge(list1, list2): 
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
        return merged_list 



    '''

    Reminder: get the variable names corrected 

    '''



    cat1=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat1.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat1.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat1[a] = [b]
        else:
            if not isinstance(cat1[a], str):
                cat1[a].append(b)


    cat2=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat2.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat2.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat2[a] = [b]
        else:
            if not isinstance(cat1[a], str):
                cat2[a].append(b)


    cat3=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat3.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat3.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat3[a] = [b]
        else:
            if not isinstance(cat1[a], str):
                cat3[a].append(b)

    cat4=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat4.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat4.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat4[a] = [b]
        else:
            if not isinstance(cat4[a], str):
                cat4[a].append(b)


    cat5=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat5.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat5.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat5[a] = [b]
        else:
            if not isinstance(cat5[a], str):
                cat5[a].append(b)

    cat6=defaultdict(list)
    with open("/Users/lichenhuilucy/Desktop/dictionaries/cat6.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1]) # append to list and update if double word token 
            else: 
                word1=singleinternalword
                cat6.update({word1:""}) # update if single word token
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            cat6[a] = [b]
        else:
            if not isinstance(cat6[a], str):
                cat6[a].append(b)


    categorieslist=[cat1,cat2,cat3,cat4,cat5,cat6]

    sentlog_outputfields=["filename","sentnolist","pcat1neutral","cat2neutral","cat3neutral","cat4neutral","cat5neutral","cat6neutral","cat1p","cat2p","cat3p","cat4p","cat5p","cat6p","cat1n","cat2n","cat3n","cat4n","cat5n","cat6n","l1c","l2c","l3c"]

    
    
    l1c=[]
    l2c=[]
    l3c=[]
    cat1neutral=[]
    cat2neutral=[]
    cat3neutral=[]
    cat4neutral=[]
    cat5neutral=[]
    cat6neutral=[]
    cat1p=[]
    cat2p=[]
    cat3p=[]
    cat4p=[]
    cat5p=[]
    cat6p=[]
    cat1n=[]
    cat2n=[]
    cat3n=[]
    cat4n=[]
    cat5n=[]
    cat6n=[]
    externalsent=[]
    internalsent=[]
    doublenegsent=[]
    posperfsent=[]
    negperfsent=[]
    positiveperformancesent=[]
    negativeperformancesent=[]
    sentnolist=[]
    filename=[]
    sentlist=[]
    sentlen=[]
    LMposall=[]
    LMnegall=[]
    possentcount=[]
    neggsentcount=[]
    positivewordscount=[]
    negativewordscount=[]
    positiveLMlist=[]
    negativeLMlist=[]



    def checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional): 
        #postemp=posperfcnt
        #negtemp=negperfcnt
        #postemp1=posperfcnt
        #negtemp1=negperfcnt
        #pos+=postemp1-postemp
        #neg+=negtemp1-negtemp

        for i in range(len(attributionlist)):
            if attributionlist[i]>=1 and posperfcnt>=1: 
                attributiondirectional[i]+=1
                attributionlist[i]-=1
                posperfcnt-=1
                

        for i in range(len(attributionlist)):
            if attributionlist[i]>=1 and negperfcnt>=1: 
                attributiondirectional[i+6]+=1
                attributionlist[i]-=1
                negperfcnt-=1
                

        return posperfcnt,negperfcnt,attributionlist,attributiondirectional


    dictcount=defaultdict(int)

    item="FILED AS OF DATE:"
    filenum=1 #correct as filenum 

    f_out=open(csv1,"w")
    wr=csv.writer(f_out)
    wr.writerow(sentlog_outputfields)
    fsent=open(direct,"w")

    for files in glob.glob(corpus):
        year=files[files.find("-")+1:files.find(".")]
        cik=files[:files.find("-")]
        with open(files) as f: 
            content = f.read()
            text1=content.lower()
            matchedstring=""
            for m in re.finditer(item.lower(), text1): 
                if not m: 
                    matchedstring="."
                    raise Error
                    #print(file)
                else:
                    substr1=text1[m.start():m.start()+30]
                    #print(substr1)
                    # may be necessary to search for end string  
                    i=0
                    while i< len(substr1) and not substr1[i].isdigit(): 
                        i+=1
                    while i< len(substr1) and substr1[i].isdigit(): 
                        matchedstring+=substr1[i]
                        i+=1
                    break
            if matchedstring:
                f1.append(matchedstring.strip())

            totalnumberofsent=0
            filenum=filenum+1 
            
            re.sub("\n","",content)
            sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
            posperfcnt=0 
            negperfcnt=0
            doubleneg=0
            LMpos=0
            LMneg=0
            sentno=0
            negativewordscnt=0
            positivewordscnt=0
            for sentences in sent: # ISSUE: need to identify individual words, modify to match regex words
                #print(sentences)
                if "liquidity and capital resources" in sentences:
                    print("Y") 
                    continue
                endext=True 
                endint=True 
                endpos=True 
                endneg=True
                endposperf=True 
                endnegperf=True 
                intext=0
                posneg=0
                sentno+=1

                                                #amended on 8 nov
                                        ###########################


                #int=0
                #ext=0
                attributionlist=[0]*6
                attributiondirectional=[0]*12

                posint=0
                negint=0
                posext=0
                negext=0
                            

                                        ###########################

                fsent.write(files)
                fsent.write(str(sentno))
                fsent.write("\n")
                ww=[]
                for r in word_tokenize(sentences): 
                    if r.isalpha(): 
                        ww.append(r)
                #ww=[w in word_tokenize(sentences) if isalpha(w)]
                #ww=[w in ww if w.isalpha()]
                if len(ww)>=1:
                    #print(ww)
                    sentnolist.append(sentno)
                    if sentno==1: 
                        filename.append(files)
                    else: 
                        filename.append("none")
                    a=0
                    i=0
                    b=0
                    
                    for item in ww: 
                        if item in posperflist: 
                            LMpos+=1
                        if item in negperflist: 
                            LMneg+=1
                    
                    while i+a+b<len(ww):
                        BOOL=True
                        for b in range(1,4):
                            for a in range(1,4):
                                if BOOL: #want the boolean because iterating from position index i
                                    for categories in range(len(categorieslist)):
                                        if i+a+b<len(ww):
                                            if ww[i].lower() in categorieslist[categories]:
                                                for el in categorieslist[categories][ww[i]]:
                                                    if BOOL:
                                                        if el!="" and i+a+b<len(ww): 
                                                            if el.lower()==ww[i+a+b]: 
                                                                i=i+a+b+1
                                                                attributionlist[categories]+=1
                                                                checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                                BOOl=False


                                                else: 
                                                    i+=1
                                                    attributionlist[categories]+=1
                                                    BOOl=False
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    break  

                                    if i+a+b<len(ww):
                                        if negperfdict.get(ww[i].lower()): 
                                            #print(i+b)
                                            #print(len(ww))
                                            # if b(i,a,b,ww,amplifierset,negperfcnt,BOOL) is not None: 
                                            #     negperfcnt,BOOL,i=b(i,a,b,ww,amplifierset,negperfcnt,BOOL)
                                            
                                            
                                            if ww[i+b] in negperfdict[ww[i].lower()]:
                                                #if negperfdict[ww[i+b]] is not None:
                                                if ww[i+a+b] in amplifierset: 
                                                    # print(ww[i:i+a+b+1]) 
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+a+1]))  
                                                    dictcount[str(ww[i:i+b+a+1])]+=1
                                                    i=i+a+b+1
                                                    negperfcnt+=1
                                                    negativewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 
                                            
                                        
                                            # elif b(i,a,b,ww,negatorset,posperfcnt,BOOL) is not None:
                                            #     posperfcnt,BOOL,i=b(i,a,b,ww,negatorset,posperfcnt,BOOL)
                                            
                                                elif ww[i+a+b] in negatorset: 
                                                    # print(ww[i:i+a+b+1]) 
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("doubleneg")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))   
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    i=i+a+b+1
                                                    posperfcnt+=1
                                                    positivewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif ww[i+a+b] in badset: 
                                                    # print(ww[i:i+a+b+1]) 
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    i=i+a+b+1
                                                    negperfcnt+=1
                                                    negativewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif ww[i+a+b] in goodset: 
                                                    # print(ww[i:i+a+b+1]) 
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    i=i+a+b+1
                                                    posperfcnt+=1
                                                    positivewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 
                                        
                                            #elif b(i,a,b,ww,negatorset,posperfcnt,BOOL):

                                            elif "." in negperfdict[ww[i].lower()] and b==3:
                                                # changed to reflect greedy appraoch 28 Sept
                                                for x in range(1,4):
                                                    if ww[i+x] in amplifierset:
                                                        negperfcnt+=1
                                                        fsent.write("negative")                                                
                                                        fsent.write(str(ww[i:i+x+1]))  
                                                        dictcount[str(ww[i:i+x+1])]+=1   
                                                        negativewordscnt+=x                           
                                                        i=i+x+1
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in negatorset:
                                                        posperfcnt+=1
                                                        fsent.write("positive")                                                
                                                        fsent.write(str(ww[i:i+x+1]))  
                                                        dictcount[str(ww[i:i+x+1])]+=1
                                                        positivewordscnt+=x
                                                        i=i+x+1
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in badset:
                                                        negperfcnt+=1
                                                        fsent.write("negative")                                                
                                                        fsent.write(str(ww[i:i+x+1]))  
                                                        dictcount[str(ww[i:i+x+1])]+=1 
                                                        negativewordscnt+=x 
                                                        i=i+x+1
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in goodset:
                                                        posperfcnt+=1
                                                        fsent.write("positive")                                                
                                                        fsent.write(str(ww[i:i+x+1]))  
                                                        dictcount[str(ww[i:i+x+1])]+=1  
                                                        positivewordscnt+=x
                                                        i=i+x+1
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        BOOl=False
                                                        break


                                        if posperdict.get(ww[i].lower()) and i+a+b<len(ww): 
                                            if ww[i+b] in posperdict[ww[i].lower()]:
                                                #if negperfdict[ww[i+b]] is not None:
                                                if ww[i+a+b] in amplifierset: 
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))  
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    i=i+a+b+1
                                                    posperfcnt+=1
                                                    positivewordscnt+=sum([a,b])
                                                    BOOl=False
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    break 
                                                
                                                elif ww[i+a+b] in negatorset: 
                                                    #print(ww[i:i+a+b+1]) 
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))    
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    negativewordscnt+=sum([a,b])
                                                    i=i+a+b+1
                                                    negperfcnt+=1
                                                    BOOl=False
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    break 
                                                elif ww[i+a+b] in badset: 
                                                    #print(ww[i:i+a+b+1]) 
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))  
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    negativewordscnt+=sum([a,b])
                                                    i=i+a+b+1
                                                    negperfcnt+=1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif ww[i+a+b] in goodset: 
                                                    #print(ww[i:i+a+b+1]) 
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))  
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    i=i+a+b+1
                                                    positivewordscnt+=sum([a,b])
                                                    posperfcnt+=1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 
                                                
                                            elif "." in negperfdict[ww[i].lower()] and b==3:
                                                for x in range(1,4):
                                                    if ww[i+x] in amplifierset:
                                                        negperfcnt+=1
                                                        fsent.write("negative")                                                
                                                        fsent.write(str(ww[i:i+x+1]))      
                                                        dictcount[str(ww[i:i+x+1])]+=1
                                                        negativewordscnt+=sum([a,b])
                                                        negativewordscnt+=x
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        i=i+x+1
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in negatorset:
                                                        posperfcnt+=1
                                                        fsent.write("doubleneg")                                                
                                                        fsent.write(str(ww[i:i+x+1]))    
                                                        dictcount[str(ww[i:i+x+1])]+=1
                                                        positivewordscnt+=x
                                                        #print(ww[i:i+b+a+1]) 
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        i=i+x+1
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in badset:
                                                        fsent.write("negative")                                                
                                                        fsent.write(str(ww[i:i+x+1]))                                                     
                                                        negperfcnt+=1
                                                        dictcount[str(ww[i:i+x+1])]+=1
                                                        #print(ww[i:i+b+a+1]) 
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        negativewordscnt+=x
                                                        i=i+x+1
                                                        BOOl=False
                                                        break
                                                    if ww[i+x] in goodset:
                                                        fsent.write("positive")                                                
                                                        fsent.write(str(ww[i:i+x+1]))                                                     
                                                        posperfcnt+=1
                                                        dictcount[str(ww[i:i+x+1])]+=1
                                                        positivewordscnt+=x
                                                        #print(ww[i:i+b+a+1]) 
                                                        checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                        i=i+x+1
                                                        BOOl=False
                                                        break


                                        if ww[i].lower() in negatorset and i+a+b<len(ww) :
                                            if negperfdict.get(ww[i+b]):
                                                if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                    fsent.write("doubleneg")
                                                    fsent.write(str(ww[i:i+a+b+1]))
                                                    #freq count increment
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    # alternative sol
                                                    positivewordscnt+=sum([a,b])
                                                    posperfcnt+=1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    i=i+a+b+1
                                                    BOOl=False
                                                    break 

                                                elif "." in negperfdict[ww[i+b]] :
                                                    fsent.write("doubleneg")
                                                    fsent.write(str(ww[i:i+b+1]))     
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    posperfcnt+=1
                                                    i=i+b+1
                                                    negativewordscnt+=b
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break
                                            
                                            if posperdict.get(ww[i+b]):

                                                if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                    fsent.write("negative")
                                                    fsent.write(str(ww[i:i+a+b+1]))       
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    negperfcnt+=1
                                                    i=i+a+b+1
                                                    negativewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif "." in posperdict[ww[i+b]] :
                                                    fsent.write("negative")
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    negativewordscnt+=sum([a,b])
                                                    negperfcnt+=1
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break
                                                

                                        if ww[i].lower() in amplifierset and i+a+b<len(ww): 
                                            if posperdict.get(ww[i+b]):

                                                if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    positivewordscnt+=sum([a,b])
                                                    posperfcnt+=1
                                                    i=i+a+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break

                                                elif "." in posperdict[ww[i+b]]:
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    positivewordscnt+=b
                                                    posperfcnt+=1                                      
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break
                                                
                                                
                                                # elif c(i,a,b,ww,negperfdict,negperfcnt,BOOL) is not None: 
                                                #     negperfcnt,BOOL,i=c(i,a,b,ww,negperfdict,negperfcnt,BOOL)
                                                #     break

                                            if negperfdict.get(ww[i+b]):  
                                                if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                    # print(ww[i:i+a+b+1])
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1]))
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    negperfcnt+=1 
                                                    negativewordscnt+=sum([a,b])
                                                    i=i+a+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif "." in negperfdict[ww[i+b]]: 
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+1]))  
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    negperfcnt+=1
                                                    negativewordscnt+=b
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOL=False
                                                    break
                                            
                                        if ww[i].lower() in badset and i+a+b<len(ww): 
                                            if posperdict.get(ww[i+b]):
                                                # if c(i,a,b,ww,posperdict,posperfcnt,BOOL) is not None: 
                                                #     posperfcnt,BOOL,i=c(i,a,b,ww,posperdict,posperfcnt,BOOL)
                                                #     break

                                            
                                                #if negperfdict[ww[i+b]] is not None:
                                                if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                        # print(ww[i:i+a+b+1])
                                                        # print(ww[i])
                                                        # print(ww[i+b])
                                                        # print(ww[i+a+b])    
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+a+1]))    
                                                    dictcount[str(ww[i:i+b+a+1])]+=1
                                                    negperfcnt+=1
                                                    i=i+a+b+1
                                                    negativewordscnt+=sum([a,b])
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break

                                                elif "." in posperdict[ww[i+b]]:
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    negativewordscnt+=b
                                                    negperfcnt+=1                                         
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break
                                                
                                                
                                                # elif c(i,a,b,ww,negperfdict,negperfcnt,BOOL) is not None: 
                                                #     negperfcnt,BOOL,i=c(i,a,b,ww,negperfdict,negperfcnt,BOOL)
                                                #     break

                                            if negperfdict.get(ww[i+b]):  
                                                if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                    # print(ww[i:i+a+b+1])
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1])) 
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    negperfcnt+=1
                                                    negativewordscnt+=sum([a,b])
                                                    i=i+a+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif "." in negperfdict[ww[i+b]]: 
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    negativewordscnt+=b
                                                    negperfcnt+=1
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOL=False
                                                    break


                                        if ww[i].lower() in goodset and i+a+b<len(ww): 
                                            if posperdict.get(ww[i+b]):
                                                # if c(i,a,b,ww,posperdict,posperfcnt,BOOL) is not None: 
                                                #     posperfcnt,BOOL,i=c(i,a,b,ww,posperdict,posperfcnt,BOOL)
                                                #     break

                                            
                                                #if negperfdict[ww[i+b]] is not None:
                                                if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                        # print(ww[i:i+a+b+1])
                                                        # print(ww[i])
                                                        # print(ww[i+b])
                                                        # print(ww[i+a+b])    
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+a+1]))    
                                                    dictcount[str(ww[i:i+b+a+1])]+=1
                                                    positivewordscnt+=sum([a,b])
                                                    posperfcnt+=1
                                                    i=i+a+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break

                                                elif "." in posperdict[ww[i+b]]:
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    positivewordscnt+=b
                                                    posperfcnt+=1                                         
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break
                                                
                                                
                                                # elif c(i,a,b,ww,negperfdict,negperfcnt,BOOL) is not None: 
                                                #     negperfcnt,BOOL,i=c(i,a,b,ww,negperfdict,negperfcnt,BOOL)
                                                #     break

                                            if negperfdict.get(ww[i+b]):  
                                                if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                    # print(ww[i:i+a+b+1])
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+a+b+1])) 
                                                    dictcount[str(ww[i:i+a+b+1])]+=1
                                                    positivewordscnt+=sum([a,b])
                                                    posperfcnt+=1
                                                    i=i+a+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOl=False
                                                    break 

                                                elif "." in negperfdict[ww[i+b]]: 
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+b+1]))
                                                    dictcount[str(ww[i:i+b+1])]+=1
                                                    positivewordscnt+=b
                                                    posperfcnt+=1
                                                    i=i+b+1
                                                    checkifdecrement(posperfcnt,negperfcnt,attributionlist,attributiondirectional)
                                                    BOOL=False
                                                    break
                                            
                        
                        
                                                # else:
                                                #     #print(ww[i:i+b+a+1])   
                                                #     #print(ww[i])
                                                #     #print(ww[i+b])
                                                #     #print(ww[i+a+b])
                                                #     i=i+b+a
                                                #     BOOl=False
                                                #     break
                                            

                                   
                        i+=1
                


                    if posperfcnt>negperfcnt: 
                        possent=1
                    else: 
                        possent=0
                    if posperfcnt<negperfcnt: 
                        neggsent=1
                    else: 
                        neggsent=0
                    if LMneg>LMpos: 
                        positiveLM=1
                    else: 
                        positiveLM=0
                    if LMneg<LMpos: 
                        negativeLM=1
                    else: 
                        negativeLM=0


# 8 Nov modifications 
################



                    neggsentcount.append(neggsent)
                    possentcount.append(possent)
                    #positiveperformancesent.append(posperfcnt)
                    #negativeperformancesent.append(negperfcnt)
                    #doublenegsent.append(doubleneg)
                    LMposall.append(LMpos)
                    LMnegall.append(LMneg)
                    positivewordscount.append(positivewordscnt)
                    negativewordscount.append(negativewordscnt)
                    positiveLMlist.append(positiveLM)
                    negativeLMlist.append(negativeLM)


                    
                    category1=0
                    category2=0
                    category3=0
                    nullist=[0]*6
                    nullist2=[0]*12
                    if attributiondirectional!=nullist2:
                        category1=1
                    elif attributionlist!=nullist: 
                        category2=1
                    else: 
                        category3=1

                    cat1neutral.append(attributionlist[0])
                    cat2neutral.append(attributionlist[1])
                    cat3neutral.append(attributionlist[2])
                    cat4neutral.append(attributionlist[3])
                    cat5neutral.append(attributionlist[4])
                    cat6neutral.append(attributionlist[5])
                    cat1p.append(attributiondirectional[0])
                    cat2p.append(attributiondirectional[1])
                    cat3p.append(attributiondirectional[2])
                    cat4p.append(attributiondirectional[3])
                    cat5p.append(attributiondirectional[4])
                    cat6p.append(attributiondirectional[5])
                    cat1n.append(attributiondirectional[6])
                    cat2n.append(attributiondirectional[7])
                    cat3n.append(attributiondirectional[8])
                    cat4n.append(attributiondirectional[9])
                    cat5n.append(attributiondirectional[10])
                    cat6n.append(attributiondirectional[11])
                    l1c.append(category1)
                    l2c.append(category2)
                    l3c.append(category3)

                    positivewordscnt=0
                    negativewordscnt=0
                    posperfcnt=0
                    negperfcnt=0
                    doubleneg=0
                    LMpos=0
                    LMneg=0
                    positiveLM=0
                    negativeLM=0
                    sentlen.append(len(ww))

                else:
                    sentno-=1   

            if DEBUG:
                if filenum==10:
                    break 
    
    sorted_x = sorted(dictcount.items(), key=operator.itemgetter(1))
    print(sorted_x)
    p=zip(filename,sentnolist,cat1neutral,cat2neutral,cat3neutral,cat4neutral,cat5neutral,cat6neutral,cat1p,cat2p,cat3p,cat4p,cat5p,cat6p,cat1n,cat2n,cat3n,cat4n,cat5n,cat6n,l1c,l2c,l3c,sentlen)
    for row in p:
        wr.writerow(row)
    print(len(f1))
    return f1




a=0 


poslist=[]
neglist=[]
filenamelist=[]
yearlist=[]
ciklist=[]
llist=[] 
l1c=[]
l2c=[]
l3c=[]
cat1neutral=[]
cat2neutral=[]
cat3neutral=[]
cat4neutral=[]
cat5neutral=[]
cat6neutral=[]
cat1p=[]
cat2p=[]
cat3p=[]
cat4p=[]
cat5p=[]
cat6p=[]
cat1n=[]
cat2n=[]
cat3n=[]
cat4n=[]
cat5n=[]
cat6n=[]


#print(len(f1))

def finalcount(f1):
    a=0 
    f1=searchwords()
    print(len(f1))
    f_out2 = open(csv2, 'w')
    wr2 = csv.writer(f_out2)
    pos=0
    neg=0
    l=0
    doubleneg=0
    lmpos=0
    lmneg=0
    lmsentencespos1=0
    lmsentencesneg1=0
    poscount=0
    poswordcount=0
    negwordcount=0
    negcount=0
    sentencescount=0
    


    with open(csv1,"r") as csvfile: 

        freader=csv.reader(csvfile)
        for row in freader:
            if "none" not in row[0] and "lucy" in row[0]: #matches a component in directory name, please change accordingly
                #print(row[0])
                everyfilename=row[0]
                #
                y=row[0][row[0].find("-")+1:row[0].find("-")+5]
                yearlist.append(y)
                st=""
                for e in row[0]: 
                    if e.isalpha() or e=="/": 
                        continue
                    elif e !="-": 
                        st+=e
                    elif e=="-": 
                        break

                cik=st
                ciklist.append(cik)

                #everyfilename=
                filenamelist.append(everyfilename)
                a=a+1
                
                if a > 1: #if more than one file has been loaded and the next line is the actual filename 
                    l1c.append(l1c1)
                    l2c.append(l2c1)
                    l3c.append(l3c1)
                    cat1neutral.append(cat1neutral1)
                    cat2neutral.append(cat2neutral1)
                    cat3neutral.append(cat3neutral1)
                    cat4neutral.append(cat4neutral1)
                    cat5neutral.append(cat5neutral1)
                    cat6neutral.append(cat6neutral1)
                    cat1p.append(cat1p1)
                    cat2p.append(cat2p1)
                    cat3p.append(cat3p1)
                    cat4p.append(cat4p1)
                    cat5p.append(cat5p1)
                    cat6p.append(cat6p1)
                    cat1n.append(cat1n1)
                    cat2n.append(cat2n1)
                    cat3n.append(cat3n1)
                    cat4n.append(cat4n1)
                    cat5n.append(cat5n1)
                    cat6n.append(cat6n1)
                    llist.append(leng1)

                cat1neutral1=0
                cat2neutral1=0
                cat3neutral1=0
                cat4neutral1=0
                cat5neutral1=0
                cat6neutral1=0
                cat1p1=0
                cat2p1=0
                cat3p1=0
                cat4p1=0
                cat5p1=0
                cat6p1=0
                cat1n1=0
                cat2n1=0
                cat3n1=0
                cat4n1=0
                cat5n1=0
                cat6n1=0
                l1c1=0
                l2c1=0
                l3c1=0
                negcount=0
                sentencescount=0
                poswordcount=0
                negwordcount=0
                lmsentencespos=0
                lmsentencesneg=0
                leng1=0

            if row[2].isdigit():
                cat1neutral1+=int(row[2])
            if row[3].isdigit(): 
                cat2neutral1+=int(row[3])
            if row[4].isdigit():
                cat3neutral1+=int(row[4])
            if row[5].isdigit(): 
                cat4neutral1+=int(row[5])
            if row[6].isdigit(): 
                cat5neutral1+=int(row[6])
            if row[7].isdigit():
                cat6neutral1+=int(row[7])
            if row[8].isdigit(): 
                cat1p1+=int(row[8])
            if row[9].isdigit():
                cat2p1+=int(row[9])
            if row[10].isdigit(): 
                cat3p1+=int(row[10])
            if row[11].isdigit(): 
                cat4p1+=int(row[11])
            if row[12].isdigit():
                cat5p1+=int(row[12])
            if row[13].isdigit(): 
                cat6p1+=int(row[13])
            if row[14].isdigit():
                cat1n1+=int(row[14])
            if row[15].isdigit():
                cat2n1+=int(row[15])
            if row[16].isdigit():
                cat3n1+=int(row[16])
            if row[17].isdigit():
                cat4n1+=int(row[17])
            if row[18].isdigit():
                cat5n1+=int(row[18])
            if row[19].isdigit():
                cat6n1+=int(row[19])
            if row[20].isdigit():
                l1c1+=int(row[20])
            if row[21].isdigit():
                l2c1+=int(row[21])
            if row[22].isdigit():
                l3c1+=int(row[22])
            if row[23].isdigit():
                leng1+=int(row[23])

            sentencescount+=1          
            """
            if "1" in row[2] and "1" in row[4]: 
                posint=posint+1
            if "1" in row[3] and "1" in row[4]: 
                negint=negint+1
            if "1" in row[2] and "1" in row[5]:
                posext=posext+1 
            if "1" in row[3] and "1" in row[5]:
                negext=negext+1
            """ 

            
    p=zip(filenamelist,yearlist,ciklist,cat1neutral,cat2neutral,cat3neutral,cat4neutral,cat5neutral,cat6neutral,cat1p,cat2p,cat3p,cat4p,cat5p,cat6p,cat1n,cat2n,cat3n,cat4n,cat5n,cat6n,l1c,l2c,l3c,llist) 
    wr2.writerow(["filename","year","cik","pcat1neutral","cat2neutral","cat3neutral","cat4neutral","cat5neutral","cat6neutral","cat1p","cat2p","cat3p","cat4p","cat5p","cat6p","cat1n","cat2n","cat3n","cat4n","cat5n","cat6n","l1c","l2c","l3c","sentlen"])
    for row in p:
        wr2.writerow(row)



finalcount(f1)