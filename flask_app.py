
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import truenet

app = Flask(__name__)
CORS(app)

test = [{'number': 14, 'name': 'Kakuna'},
           {'number': 16, 'name': 'Pidgey'},
           {'number': 50, 'name': 'Diglett'}]


class MyApp(Resource):
    def get(self):
        return test

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True, location='json')
        args = parser.parse_args(strict=True)
        ans = truenet.analyze(args['query'])
        #ans = {"usage": {"text_characters": 58, "features": 2, "text_units": 1}, "keywords": [{"relevance": 0.935399, "text": "Donald Trump", "sentiment": {"score": 0.431597}, "emotion": {"anger": 0.083028, "joy": 0.461943, "sadness": 0.074047, "fear": 0.038384, "disgust": 0.126171}}, {"relevance": 0.918118, "text": "Linkin Park Concert", "sentiment": {"score": 0.431597}, "emotion":{"anger": 0.083028, "joy": 0.461943, "sadness": 0.074047, "fear": 0.038384, "disgust": 0.126171}}], "percentage": 74.0, "language": "en", "entities": [{"emotion": {"anger": 0.083028, "joy": 0.461943, "sadness": 0.074047, "fear": 0.038384, "disgust": 0.126171}, "count": 1, "sentiment": {"score": 0.431597}, "text": "Donald Trump", "disambiguation": {"subtype": ["AwardNominee", "AwardWinner", "Celebrity", "CompanyFounder", "TVPersonality", "TVProducer", "FilmActor", "TVActor"], "name": "Donald Trump", "dbpedia_resource": "http://dbpedia.org/resource/Donald_Trump"}, "relevance": 0.33, "type": "Person"}, {"emotion": {"anger": 0.083028, "joy": 0.461943, "sadness": 0.074047, "fear": 0.038384, "disgust": 0.126171}, "count": 1, "sentiment": {"score": 0.431597}, "text": "Pink Floyd", "type" : "Music Band"}]}
        return ans

api = Api(app)
api.add_resource(MyApp, '/api/v1/analyze')

@app.route('/')
def home():
    return "Home"

@app.route('/hello')
def hello():
    return "Hello"

