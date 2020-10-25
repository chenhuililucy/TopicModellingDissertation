
# Output main 

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

#https://stackoverflow.com/questions/45145368/python-scikit-learn-get-documents-per-topic-in-lda

os.chdir("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic")

import gensim
from gensim.utils import simple_preprocess

file=[]
corpus=[]

d=defaultdict(list)
i=0
for files in glob.glob("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 
      i+=1
      d[i]=files
      print(files)
        #files.encode('utf-8').strip()
      lineList = f.readlines()
      #if debug1:
        #print(lineList)
      lines1="".join(lineList) 
      lines = re.sub(r'\d', '', lines1)
      #if debug1:
        #print(lines)
      corpus.append(lines)
      #if debug2:
        #print(corpus)


# Initialise the count vectorizer with the English stop words
count_vectorizer = CountVectorizer(stop_words='english')
# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(corpus)
# Visualise the 10 most common words
#plot_10_most_common_words(count_data, count_vectorizer)

import warnings
warnings.simplefilter("ignore", DeprecationWarning)
# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA
 
# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        
# Tweak the two parameters below
number_topics = 25
number_words = 20
# Create and fit the LDA model
lda = LDA(n_components=number_topics, n_jobs=-1)
lda.fit(count_data)
doc_topic = lda.transform(count_data)

l1=[]
l2=[]
for n in range(doc_topic.shape[0]):
    topic_most_pr = doc_topic[n].argmax()
    l1.append(d[n-1])
    l2.append(topic_most_pr)
    print("doc: {} topic: {}\n".format(d[n+1],topic_most_pr))

z=zip(l1,l2)

with open("topics.csv","w") as f_out: 
  wr=csv.writer(f_out)
  for row in z: 
    wr.writerow(row)

# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)



#%%time
from pyLDAvis import sklearn as sklearn_lda
import pickle 
import pyLDAvis
LDAvis_data_filepath = os.path.join('./ldavis_prepared_'+str(number_topics))
# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
#if 1 == 1:
LDAvis_prepared = sklearn_lda.prepare(lda, count_data, count_vectorizer)
with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)
        
# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath,"rb") as f:
    LDAvis_prepared = pickle.load(f)
pyLDAvis.save_html(LDAvis_prepared, './ldavis_prepared_'+ str(number_topics) +'.html')


#lda = models.LdaModel.load('lda.model')

for i in range(0, 26):
    with open('output_file.txt', 'w') as outfile:
        outfile.write('{}\n'.format('Topic #' + str(i + 1) + ': '))
        for word, prob in lda.show_topic(i, topn=20):
            outfile.write('{}\n'.format(word.encode('utf-8')))
        outfile.write('\n')