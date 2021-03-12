

'''

Find trend in between emerging topics, content and performance 


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



def search(startdate, enddate, lookup, tags):
    currdirectory='/Users/lichenhuilucy/Desktop/new'
    for yeardate in range(startdate, enddate):
        filelist=[]
        yearlist=[]
        ciklist=[]
        lenlist=[]
        for files in glob.glob("/Users/lichenhuilucy/Desktop/newdic/*.txt"):
            #print(files)
            if int(re.sub("[^0-9]", "",files[files.find("-")+1:files.find(".")]))==yeardate:
                with open(files) as f: 
                    
                    lineList = f.readlines()
                    lines1="".join(lineList) 
                    w=True 
                    for i in lookup: 
                        if i not in lines1: 
                            w=False
                    if w: 
                        print("y")
                        year=files[files.find("-")+1:files.find(".")]
                        year=re.sub("[^0-9]", "", year)
                        yearlist.append(year)
                        cik=files[:files.find("-")]
                        cik=re.sub("[^0-9]", "", cik)
                        ciklist.append(cik)
                        filelist.append(files)
        
    z=zip(filelist,ciklist)
    #print(os.listdir(currdirectory))
    with open('/Users/lichenhuilucy/Desktop/new'+tags,"w") as f:
        fwriter=csv.writer(f)
        for row in z:
            fwriter.writerow(row)
        f.close()
    print(f)




def mergecsv(labels):
    currdirectory='/Users/lichenhuilucy/Desktop/new'
    ciks=[]
    with open(currdirectory+labels,"r") as f: 
        freader=csv.reader(f)
        for row in freader: 
            if row!="cik":
                ciks.append(row[1])
        f.close()
    
    fin=[]
    with open("/Users/lichenhuilucy/Desktop/research/vectorfinalv7finalv.csv","r") as final: 
        freader=csv.reader(final)
        for row in freader: 
            if row[2] in ciks or row[2]=="cik": 
                if row[12]!=".":
                    fin.append(row)
        f.close()
    
    with open(currdirectory+"/f"+labels,"w") as final: 
        fwriter=csv.writer(final)
        for row in fin:
            fwriter.writerow(row)
        f.close()

    

def plotgraphs(labels):
    currdirectory='/Users/lichenhuilucy/Desktop/new'
    new=pd.read_csv(currdirectory+"/f"+labels)
    prepared=new.reset_index().pivot_table(index="year",columns="cik", values="roa")
    prepared.to_csv(currdirectory+"prepared.csv", index=True)
    prepared = prepared.fillna(method="ffill").fillna(0)
    preparedT = prepared.T
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(prepared)

    '''
    scores = []
    for k in range(2, 5):
        print(k)
        model = TimeSeriesKMeans(n_clusters=k, metric="dtw", verbose=False, max_iter_barycenter=10, n_init=5, max_iter=50, random_state=0).fit(preparedT.values[...,:])
        scores.append(silhouette_score(prepared.values, model.labels_, metric="dtw"))
    '''

    best_num_cluster = 3
    print(best_num_cluster)
    model = TimeSeriesKMeans(n_clusters=best_num_cluster, metric="dtw", verbose=False, max_iter_barycenter=10, n_init=5, max_iter=50, random_state=0).fit(preparedT.values[...,:])
    print(model.labels_)

    df_labels = pd.DataFrame(model.labels_, index=preparedT.index, columns=["Cluster"])
    print(df_labels.head())
    df_labels.to_csv(currdirectory+"/cluster"+labels, index=True)
    fig, axs =  plt.subplots(1, 3, figsize=(48, 9))

    '''

    for yi in range(best_num_cluster):
        ax = axs[yi]
        cluster_series = preparedT[df_labels["Cluster"] == yi]
        for xx in cluster_series.index:
            cluster_series.loc[xx].plot(ax=ax, color="k", alpha=.2)
        
        ax.plot(model.cluster_centers_[yi].ravel(), color="r")
        ax.set_xlim([1995,2019])
        ax.set_ylim([-4,4])

        ax.tick_params(axis='y', which='major', labelsize=15)
        ax.tick_params(axis='x', which='major', labelsize=15, rotation=45)
        
        ax.set_xlabel("")
        anc = AnchoredText("({})".format(yi+1), loc="upper right", frameon=False, prop=dict(fontweight="bold", fontsize=50))

        ax.add_artist(anc)
    fig.tight_layout()
    plt.savefig(currdirectory+labels[:-4]+".png", dpi=600, bbox_inches='tight')
    plt.show()

    prepared.plot(grid=True,legend=False)
    axes = plt.gca()
    axes.set_xlim([1995,2019])
    axes.set_ylim([-4,4])
    plt.savefig(currdirectory+labels[:-4]+"1.png", dpi=600, bbox_inches='tight')
    plt.show()

    '''

    '''


    rows=[]

    with open(currdirectory+"/f"+labels,"r") as final: 
        freader=csv.reader(final)
        for row in freader:
            rows.append(row)
        final.close()

    rows[0].append("labels")
    for i in range(1,len(rows)):
        try: 
            rows[i]=rows[i].append(model.labels_[i-1])
        except IndexError: 
            print(i)

    with open(currdirectory+"/cluster"+labels,"w") as final: 
        fwriter=csv.writer(final)
        for row in rows:
            fwriter.writerow(row)
        final.close()
    '''



#startdates=[1995,1999,2004]
startdates=[1999]
#labels=["/mexicopesos.csv","/dot_com_bubble.csv","/yankee_abandonment.csv"]
labels=["/dot_com_bubble.csv"]
#lookup=[["peso"],["software"],["yankee"]]
lookup=[["software"]]

for i in range(len(startdates)):
    search(startdates[i], startdates[i]+1, lookup[i], labels[i])
    mergecsv(labels[i])
    plotgraphs(labels[i])


