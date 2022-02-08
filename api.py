import json
#from urllib import response
import request
import pprint

from credentials import *
api_key = key

TRANSCRIPT_ENDPOINT = ''

response = request.post(
    
      TRANSCRIPT_ENDPOINT,
      headers={'authorization': api_key, 'content-type': 'application/json'},
      json={
          'audio_url " ''
          'sentiment_analysis': True  
      },  

)

response_json = response.json()
print(pprint.pprint(response_json))

