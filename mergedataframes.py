


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
import pandas as pd 
import matplotlib.pyplot as plt


finaloutput = pd.read_csv("/Users/lichenhuilucy/Desktop/test1/vectorfinal.csv")
mexicopesos = pd.read_csv("/Users/lichenhuilucy/Desktop/test1/mexicopesos1.csv")
new=pd.concat(finaloutput,mexicopesos,on=["cik"],how="outer")
prepared=new.pivot(index="year",columns="cik", values="roa")
print(prepared)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(prepared)
#prepared = prepared.fillna(method="ffill").fillna(0)

prepared.plot(grid=True)
axes = plt.gca()
axes.set_xlim([1995,2019])
axes.set_ylim([-2,2])
plt.show()




