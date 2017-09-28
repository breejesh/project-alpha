import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

class Response(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="b6285e8a-94f0-4e93-a272-e8544d44714d",
  password="JWIggRdPnWMf",
  version="2017-02-27")

def watson_analyses(query):
  try:
      response = natural_language_understanding.analyze(
        text=query,
        features=[
          Features.Entities(
            emotion=True,
            sentiment=True,
            limit=4
          ),
          Features.Keywords(
            emotion=True,
            sentiment=True,
            limit=4
          )
        ]
      )
  except Exception, e:
      response = {}
  return response

def analyze(query, value, sources):
    response = watson_analyses(query)
    respDict = json.loads(json.dumps(response))
    respDict['percentage'] = value
    respDict['sources'] = sources
    return respDict

