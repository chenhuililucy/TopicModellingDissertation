




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
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from itertools import chain
import gensim
from gensim.utils import simple_preprocess
from gensim import corpora


''''

Second run: cosine similarities to deduce the most topic with the 
smaller the angle, the higher the cosine similarity
For any year, to deduce the topic with the lowest cosine similarity with ALL of the topics in the previous year
By just taking the mean 
Print this topic out

''''



d=defaultdict(list)
# modification : store cik, year, filelength
print("executing")


def loaddata():

    #initalize matrix (dimensions) ############################################################
    
    matrix = [[0 for x in range(25)] for y in range(25)]

    #Load data ############################################################################

    for files in glob.glob("/Users/lichenhuilucy/Desktop/newdic/*.txt"):
        for yeardate in range(1994,2019):
            corpus=[]
            if re.sub("[^0-9]", "",files[files.find("-")+1:files.find(".")])==yeardate:
                with open(files) as f: 
                    lineList = f.readlines()
                    lines1="".join(lineList) 
                    lines = re.sub(r'\d', '', lines1) #rid numbers
                    corpus.append(lines)

            # LDA part ############################################################################

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

            # Compute cosine similarities #########################################################

            # want a current vector 

            simMatrixCos = []
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



