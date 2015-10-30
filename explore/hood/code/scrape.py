
import pymongo
from pymongo import MongoClient
import requests

from wsapi import WSAPI


apikey = WSAPI
lat = 
lon = 

requrl = 'http://api.walkscore.com/score'
payload = {'wsapikey':apikey,
		   'lat': lat,
		   'lon': lon,
		   'format': 'JSON'}

response = requests.get(requrl, params = payload)

client = MongoClient()
# Initiate Database
db = client['hood']
# Initiate Table
table = db['ws']