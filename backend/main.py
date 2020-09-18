from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import pickle
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
import nltk
from flask_cors import CORS, logging

app = Flask(__name__)
CORS(app)
api = Api(app)

model = pickle.load(open('Data/logisticRegression.pkl', 'rb'))
countVec = pickle.load(open('Data/tfidf_vectorizer.pkl', 'rb'))


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


class Model(Resource):
    def post(self):
        data = request.get_json()
        if(len(data['lyric']) < 50):
            abort(401, message='Isso é uma letra de música?')
        final_features = countVec.transform([data['lyric']])
        prediction = model.predict(final_features)
        if prediction == 1:
            return jsonify({'genre': 'Bossa Nova'})
        elif prediction == 2:
            return jsonify({'genre': 'Funk'})
        elif prediction == 3:
            return jsonify({'genre': 'Gospel'})
        elif prediction == 4:
            return jsonify({'genre': 'Sertanejo'})
        else:
            abort(402, message='Genero da música não suportado')


api.add_resource(Model, '/model/submit')

if __name__ == '__main__':
    app.run(debug=True)