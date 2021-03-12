


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
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

import numpy as np
import pandas as pd
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable

import country_converter as coco
cc = coco.CountryConverter()
import datetime
from isoweek import Week

from statsmodels.tsa.stattools import grangercausalitytests
from tslearn.clustering import TimeSeriesKMeans, KernelKMeans, silhouette_score
from tslearn.metrics import gak, sigma_gak

metrics="/Users/lichenhuilucy/Desktop/test1/name6.csv"
dotcom="/Users/lichenhuilucy/Desktop/new/cluster/dot_com_bubble.csv"
final="/Users/lichenhuilucy/Desktop/research/vectorfinalv7finalv.csv"
currdirectory='/Users/lichenhuilucy/Desktop/new'


'''
metricscsv = pd.read_csv(metrics)
dotcomcsv = pd.read_csv(dotcom)
finalf = pd.read_csv(final)
new=pd.merge(metricscsv,dotcomcsv,on=["cik"],how="right")
print(new.head())
new1=pd.merge(new,finalf,on=["cik","year"],how="right")
print(new1.head())
new1.to_csv(currdirectory+"/final1.csv", index=True)
'''


def preparedataframe():
    newframe=pd.read_csv("/Users/lichenhuilucy/Desktop/new/newdataframe.csv")
    newdata1=newframe.loc[newframe["Cluster"]==2]
    newdata2=newframe.loc[newframe["Cluster"]==1]
    newdata3=newframe.loc[newframe["Cluster"]==0]
    #print(newdata3.head())
    return newdata1, newdata2, newdata3


def pivotdataframes(value2,newdata3):
    newdata3=newdata3.fillna(method="ffill").fillna(0)
    newdata3.dropna(subset=["year","cik"])
    newdata3 = newdata3[newdata3.year != "."]
    newdata3 = newdata3[newdata3.cik != "."]
    newdata3 = newdata3[newdata3.roa != "."]
    newdata3["roa"] = pd.to_numeric(newdata3["roa"], downcast="float") # turn datatype to float
    piv1 = newdata3.pivot_table(index="cik", columns="year", values="roa") # default being mean 
    #newpiv1=pd.DataFrame(piv1.mean().to_dict(),index=[piv1.index.values[-1]]) #calculate the mean of the roa across each year
    newpiv1=pd.DataFrame(piv1.mean())
    newpiv1 = newpiv1.fillna(method="ffill").fillna(0)
    piv2 = newdata3.reset_index().pivot_table(index="cik", columns="year", values=value2)
    newpiv2=piv2.mean()
    #newpiv2=pd.DataFrame(piv2.mean().to_dict(),index=[piv2.index.values[-1]]) #calculate the mean of the roa across each year
    newpiv2 = newpiv2.fillna(method="ffill").fillna(0)
    #print(newpiv1)
    #print(newpiv2)
    return newpiv1,newpiv2 

def printtrendline(newdata3,cnt):
    newdata3=newdata3.fillna(method="ffill").fillna(0)
    newdata3.dropna(subset=["year","cik"])
    newdata3 = newdata3[newdata3.year != "."]
    newdata3 = newdata3[newdata3.cik != "."]
    newdata3 = newdata3[newdata3.roa != "."]
    print(newdata3.head())
    newdata3["roa"] = pd.to_numeric(newdata3["roa"], downcast="float") # turn datatype to float
    piv1 = newdata3.pivot_table(index="cik", columns="year", values="roa") # default being mean     df.plot(grid=True,legend=False)
    piv1=pd.DataFrame(piv1.mean())
    piv1.plot(legend=False)
    print(piv1.head())
    axes = plt.gca()
    axes.set_xlim([1995,2019])
    axes.set_ylim([-0.2,0.2])
    plt.savefig("/Users/lichenhuilucy/Desktop/new"+str(cnt)+".png", dpi=600, bbox_inches='tight')
    plt.show()


def grangercausality(df1,df2): 
    X = pd.concat([df1, df2], axis=1)
    pearson = X.corr().iloc[0, 1]
    rows=[]
    max_lag=5
    res = grangercausalitytests(X, maxlag=max_lag, verbose=False)
    val = []
    for i in range(max_lag):
        val.append((res[i+1][0]['ssr_ftest'][0], res[i+1][0]['ssr_ftest'][1], res[i+1][0]['ssr_ftest'][-1]))
    val.sort(key=lambda x:x[0], reverse=True)
    row = [pearson, *val[0]]
    rows.append(row)
    results = pd.DataFrame(rows, columns=["Pearson Corr", "F-Score", "p-Value", "LAG"])
    print(results)



df1,df2,df3=preparedataframe()
d=[df1,df2,df3]
cnt=0
for i in d:
    cnt+=1
    printtrendline(i,cnt)
d=[df3]
#dic={df1:3, df2:2, df3: 1}
l=["cat1p","cat2p","cat3p","cat4p","cat5p","cat6p","cat1n","cat2n","cat3n","cat4n","cat5n","cat6n"]

for entry in l:
    i=3
    for dataframe in d:
        try:
            df1n,df2n=pivotdataframes(entry,dataframe)
            print(entry,i)
            grangercausality(df2n,df1n)
        except ValueError: 
            pass
        i-=1



