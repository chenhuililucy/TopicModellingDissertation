


'''

Baseline LDA model that graphs document length count


'''



import os 
import glob
import re
import csv
import nltk 
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from collections import defaultdict
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams
import matplotlib.pyplot as plt
from scipy.stats import zipf
import csv
import math
import re
import sys
import os
import nltk
import pandas as pd
from operator import itemgetter
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from itertools import chain
import gensim
from gensim.utils import simple_preprocess
from gensim import corpora
import numpy as np



file=[]
corpus=[]
flist=[]#store filenames


count=0
d=defaultdict(list)

# modification : store cik, year, filelength
print("executing")


def loaddata():
    i=0
    for files in glob.glob("/Users/lichenhuilucy/Desktop/newdic/*.txt"):
        with open(files) as f: 
            i+=1
            if i==10000: 
                break

            flist.append(files)
            lineList = f.readlines()
            lines1="".join(lineList) 
            lines = re.sub(r'\d', '', lines1)
            corpus.append(lines)
            sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',lines)
            l=len(sent)
            d[files]=l           


def plotgraph(xs,a): 
    xs=np.array(xs)
    ys=np.array([i for i in range(1994,2019)])
    plt.plot(ys,xs)
    axes.set_xlabel('Time')
    axes.set_ylabel('Median Disclosure Length')
    titlestring="Cluster"+a
    axes.set_title(titlestring)
    plt.show()
    


def LDAmodel():

    loaddata()
    texts = [[word for word in document.lower().split() if word not in stopwords.words('english') and word.isalpha()]
            for document in corpus]


    # remove words that appear only once
    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]

    # Create Dictionary.
    id2word = corpora.Dictionary(texts)
    # Creates the Bag of Word corpus.
    mm = [id2word.doc2bow(text) for text in texts]


    lda = LdaModel(corpus=mm, id2word=id2word, num_topics=25, \
                                update_every=1, chunksize=10000, passes=5,minimum_probability=0)

    lda_corpus = lda[mm]

    # Find the threshold, let's set the threshold to be 1/#clusters,
    # To prove that the threshold is sane, we average the sum of all probabilities:
    scores = list(chain(*[[score for topic_id,score in topic] \
                        for topic in [doc for doc in lda_corpus]]))
    threshold = sum(scores)/len(scores)
    #print(threshold)

    #print(lda_corpus)

    for word in lda.print_topics(num_words=30): 
        print(word)

    N=25

    fin=[]
    indexes=[]
    fin2=[]
    for index in range(0,N):
        cluster1 = [j for i,j in zip(lda_corpus,flist) if i[index][1] > threshold] # this is the document name 
        cluster2 = [i[index][1] for i,j in zip(lda_corpus,flist) if i[index][1] > threshold] # this is the %certainty that we know that a certain document belongs to a certain cluster
        for elements in cluster1: 
            fin.append(elements) 
            indexes.append(index) # this is the cluster name 
        for e in cluster2:
            fin2.append(e)


    yearlist=[]
    ciklist=[]
    lenlist=[]
    for files in fin:
        year=files[files.find("-")+1:files.find(".")]
        year=re.sub("[^0-9]", "", year)
        yearlist.append(year)
        cik=files[:files.find("-")]
        cik=re.sub("[^0-9]", "", cik)
        ciklist.append(cik)
        lenlist.append(d[files])

    z=zip(fin,ciklist,yearlist,indexes,fin2,lenlist)
    #z=sorted(z, key=itemgetter(5)) # smallest numbers first
    #z=sorted(z, key=itemgetter(2))

                            
    with open("LDAtopics(1).csv","w") as f:
        fwriter=csv.writer(f)
        for row in z:
            fwriter.writerow(row)


    # then need the median len
    cat=[]  # want to be appending sub list to this overall list  
    # startingyear = 1993 
    for a in range(0,25): 
        newlist=[]
        for i in range(25): 
            newlist.append([])
        for b in range(1994,2019): 
            for i in range(len(z)): #loop through the list for every year and every category
                print(z[i][3])
                print(z[i][2])
                if a==int(z[i][3]) and b==int(z[i][2]): 
                    print("y")
                    newlist[b-1994].append(z[i][5])
        print(newlist)
        median=[]
        for sublist in newlist: 
            if sublist is not None:
                median.append(np.median(sublist)) # median for each category for each year
        print(median)
        plotgraph(median,a) # plot graph for each category 
        cat.append(median)

    print(cat)


LDAmodel()