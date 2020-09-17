from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

df = pd.read_csv('Data/final.csv', index_col=0)
y = []
X = []

for index, row in df.iterrows():
    y.append(row[1])
    X.append(row[0])

countVec = TfidfVectorizer(
    stop_words=stopwords.words('portuguese'), sublinear_tf=True)

X = countVec.fit_transform(X)

pickle.dump(countVec, open('tfidf_vectorizer.pkl', 'wb'))

lr = LogisticRegression(max_iter=500)

lr.fit(X, y)

pickle.dump(lr, open('logisticRegression.pkl', 'wb'))
