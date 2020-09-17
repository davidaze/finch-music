from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import pickle

app = Flask(__name__)
api = Api(app)

model_post_args = reqparse.RequestParser()
model_post_args.add_argument(
    'lyric', type=str, help='Utilize esta variável com a Letra da Música como conteúdo', required=True)

model = pickle.load(open('logisticRegression.pkl', 'rb'))
countVec = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))


def clean_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace('.', '')
    return text


class Model(Resource):
    def post(self):
        args = model_post_args.parse_args()
        features = [clean_text(args.lyric)]
        final_features = countVec.transform(features)
        prediction = model.predict(final_features)
        if prediction == 1:
            return {'genero': 'Bossa Nova'}
        elif prediction == 2:
            return {'genero': 'Funk'}
        elif prediction == 3:
            return {'genero': 'Gospel'}
        elif prediction == 4:
            return {'genero': 'Sertanejo'}
        else:
            abort(401, message='Genero da música não suportado')


api.add_resource(Model, '/model')


if __name__ == '__main__':
    app.run(debug=True)
""
