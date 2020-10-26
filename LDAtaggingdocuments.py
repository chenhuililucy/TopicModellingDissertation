
import os 
import glob
import re
import re
import glob
import os
import csv
import nltk 
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import re
import glob
import os
import csv
import nltk 
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from itertools import chain

os.chdir("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic")

import gensim
from gensim.utils import simple_preprocess
from gensim import corpora


file=[]
corpus=[]
flist=[]#store filenames

count=0
d=defaultdict(list)
for files in glob.glob("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 
        #count+=1
        #if count==10: 
            #break
        flist.append(files)
            #files.encode('utf-8').strip()
        lineList = f.readlines()
        #if debug1:
            #print(lineList)
        lines1="".join(lineList) 
        lines = re.sub(r'\d', '', lines1)
        #if debug1:
            #print(lines)
        corpus.append(lines)
        d[lines]=files

        #if debug2:
            #print(corpus)

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
print(threshold)

print(lda_corpus)
#

# l1=[]
# l2=[]
# for n in range(25):
#     topic_most_pr = lda_corpus[n].argmax()
#     l1.append(d[n-1])
#     l2.append(topic_most_pr)
#     print("doc: {} topic: {}\n".format(d[n+1],topic_most_pr))

#for i in  lda.show_topics():
    #print i[0], i[1]


for word in lda.print_topics(num_words=30): 
    print(word)

fin=[]
indexes=[]
fin2=[]
for index in range(0,25):
    cluster1 = [j for i,j in zip(lda_corpus,flist) if i[index][1] > threshold]
    cluster2 = [i[index][1] for i,j in zip(lda_corpus,flist) if i[index][1] > threshold]
    for elements in cluster1: 
        fin.append(elements)
        indexes.append(index)
    for e in cluster2:
        fin2.append(e)

z=zip(fin,indexes,fin2)

with open("LDAtopics.csv","w") as f:
    fwriter=csv.writer(f)
    for row in z:
        fwriter.writerow(row)