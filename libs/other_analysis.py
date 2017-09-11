import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

class Response(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="9ebd6c29-f3f3-462a-800d-764229422282",
  password="FJVM0P5ccuFP",
  version="2017-02-27")

def watson_analyses(query):
    response = natural_language_understanding.analyze(
      text=query,
      features=[
        Features.Entities(
          emotion=True,
          sentiment=True,
          limit=2
        ),
        Features.Keywords(
          emotion=True,
          sentiment=True,
          limit=2
        )
      ]
    )
    return response

def analyze(query, value):
    response = watson_analyses(query)
    respDict = json.loads(json.dumps(response))
    respDict['percentage'] = value
    return respDict

