#allows to execute get and post
import requests
#import oauth related library
from requests_oauthlib import OAuth1
#able to easily twitter api outputs
import json
#encodes a query string into a proper request url
from urllib.parse import urlparse
#create authenticated connection with keys
#1. api key 2. api secret key 3. access token 4. access token secret

#the endpoints for REST API and Streaming API
url_rest='https://api.twitter.com/1.1/search/tweets.json'
#searching for twitterdev and new and premium
url_resting='https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium'
#streaming api
url_streaming='https://stream.twitter.com/1.1/statuses/sample.json'

params = {'api_key':'vFutoJoPIDaF8O3U3ifJUnrFw',
'api_secret_key':'Gfy8ykTjnHf7gxj0kkakRWqY9gWhDEd69aHDWewAWP2hsxCv0z',
'access_token':'855588527039422465-BirmEI78Vvugvm44y5cJzNoMjPiF8B8',
'access_token_secret':'RjZhI9lCoptKipRcKnPV6Uu4mIa4L0CGk9FoBXJ7GJNnB'}

auth=OAuth1(params['api_key'],params['api_secret_key'],
params['access_token'],params['access_token_secret'])

#encode query searching for 3 car brands
q=urlparse('BMW OR Mercedes OR Audi')

#make a search request
results=requests.get(url_resting,auth=auth)
#request returns list of tweets with all meta info. convert it to json
#and print each tweet under the text field

#returns meta information
#print(results.json())

for tweet in results.json():
    print(tweet)
#returns > statuses and metadata 
