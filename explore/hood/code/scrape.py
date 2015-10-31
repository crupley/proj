
import pymongo
from pymongo import MongoClient
import requests

from wsapi import WSAPI


apikey = WSAPI
lat = 37.7700103
lon = -122.4535951

requrl = 'http://api.walkscore.com/score'
payload = {'wsapikey':apikey,
		   'lat': lat,
		   'lon': lon,
		   'format': 'json'}

response = requests.get(requrl, params = payload)

client = MongoClient()
# Initiate Database
db = client['hood']
# Initiate Table
table = db['ws']