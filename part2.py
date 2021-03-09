




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
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
from operator import itemgetter
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from itertools import chain
import gensim
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import interfaces, utils, matutils



'''

Second run: cosine similarities to deduce the most topic with the 
smaller the angle, the higher the cosine similarity
For any year, to deduce the topic with the lowest cosine similarity with ALL of the topics in the previous year
By just taking the mean 
Print this topic out

'''



d=defaultdict(list)
# modification : store cik, year, filelength
print("executing")


def lda():

    
    #initalize matrix (dimensions) ############################################################
    
    #matrix = [[0 for x in range(25)] for y in range(25)]

    #Load data ############################################################################

    for yeardate in range(2000,2002):
        i=0
        corpus=[]
        flist=[]
        for files in glob.glob("/Users/lichenhuilucy/Desktop/newdic/*.txt"):

            
            #if i==100: 
                #continue
            flist.append(files)
            if int(re.sub("[^0-9]", "",files[files.find("-")+1:files.find(".")]))==yeardate:
                i+=1
                print("y")
                with open(files) as f: 
                    lineList = f.readlines()
                    lines1="".join(lineList) 
                    lines = re.sub(r'\d', '', lines1)
                    corpus.append(lines)
                    sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',lines)
                    l=len(sent)
                    d[files]=l           


                if i==300: 

                # LDA part ############################################################################

                # remove words that appear only once

                    texts = [[word for word in document.lower().split() if word not in stopwords.words('english') and word.isalpha()]
                            for document in corpus]      

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

                    # Compute cosine similarities #########################################################

                    # want a current vector 

                    #simMatrixCos = []

                    if yeardate==2000: 
                        present=[]
                        for x in range(0,25): 
                            present.append([])
                            ldaVec1 = lda.get_topic_terms(x, topn = 1000) # returns list of (int, float)
                            for item1 in ldaVec1: 
                                present[x].append(item1)
                        # now we have a list of [[(int, float)],[(int, float)],[(int, float)],...]
                        #print(present)
                    else: 
                        new=[]
                        overall=[]
                        for y in range(0,25):
                            #topicMatrixCos=[]
                            temp=[] # created for each of the 25 topics to store the mean 
                            ldaVec2 = lda.get_topic_terms(y, topn = 1000) 
                            new.append(ldaVec2)
                            for item in present:
                                sim = matutils.cossim(item, ldaVec2)
                                temp.append(sim) # temp append the similarity 
                                #simDict = (x, y, sim, ldaVec2)
                                #topicMatrixCos.append(simDict)
                            # compute mean cosine similarity 
                            av=sum(temp)/len(temp)
                            overall.append((av,y,ldaVec2)) # want to have the average cosine similarity fpr each current topic with prev
                        l=sorted(overall, key=itemgetter(0), reverse=True) # list is descending, from largest to smallest, we want lowest cosine similarity
                        #print(l)
                        #l=sorted(topicMatrixCos, key=itemgetter(2), reverse=True) 
                        print(l[-1])
                        w=lda.print_topic(l[-1][1],topn=1000)
                        print(w)
                        present=new
                        #print(present)

                    break


'''
            for x in range(0,N):
                topicMatrixCos = []
                for y in range(0,N): #want to come from the previous year
                    vec1 = lda.get_topic_terms(x, topn=model.num_terms)
                    ldaVec1 = lda.get_topic_terms(x, topn = M) # M being the number of terms in the topic model
                    ldaVec2 = lda.get_topic_terms(y, topn = M)
                    sim = matutils.cossim(ldaVec1, ldaVec2)
                    topicMatrixCos.append(simDict)
                l=sorted(topicMatrixCos, key=itemgetter(2), reverse=True)
                print(l[0])

            for word in lda.print_topics(num_words=30): 
                print(word)
                        


def consinesim(N=25,M=100):
    simMatrixCos = []
    for x in range(0,N):
        topicMatrixCos = []
        for y in range(0,N): #want to come from the previous year
            vec1 = lda.get_topic_terms(x, topn=model.num_terms)
            ldaVec1 = lda.get_topic_terms(x, topn = M) # M being the number of terms in the topic model
            ldaVec2 = lda.get_topic_terms(y, topn = M)
            sim = matutils.cossim(ldaVec1, ldaVec2)
            print(x)
            print(y)
            print(sim)
            simDict = (x, y, sim)
            topicMatrixCos.append(simDict)

        l=sorted(topicMatrixCos, key=itemgetter(2), reverse=True)
        l[0] 
        simMatrixCos.append(l) # largest numbers first
        # we want smallest number 

'''

lda()