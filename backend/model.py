from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
print('\nLoading model')
df = pd.read_csv('./Data/final.csv', index_col=0)
y = []
X = []

for index, row in df.iterrows():
    y.append(row[1])
    X.append(row[0])

def tokenize(text):
    text = text.replace('\n',' ')
    text = text.replace('  ',' ')
    text = text.lower()
    text = text.replace(',','')
    text = text.replace('?','')
    text = text.replace('!','')
    text = text.replace('.','')
    stopwordslist = stopwords.words('portuguese')
    stemmer = RSLPStemmer()
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token not in stopwordslist]
    stems = [stemmer.stem(item) for item in tokens]
    return stems
    
print('\nPreparing Data')
countVec = TfidfVectorizer(
    tokenizer=tokenize, sublinear_tf=True)

X = countVec.fit_transform(X)

pickle.dump(countVec, open('./Data/tfidf_vectorizer.pkl', 'wb'))
print('\nFitting model')
lr = LogisticRegression(max_iter=500)

lr.fit(X, y)

pickle.dump(lr, open('./Data/logisticRegression.pkl', 'wb'))
print('\nDone')