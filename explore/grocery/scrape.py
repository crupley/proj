


from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

from code.f2f import f2fapi



#f2f
def f2fquery(sort='r', page=1, apikey=f2fapi.key):
	#http://food2fork.com/about/api
	#requrl = 'http://food2fork.com/api/search?key={%s}&sort=%s&page=%d' % \
	#		 (apikey, sort, page)
	requrl = 'http://food2fork.com/api/search'
	payload = {'key':apikey,
			   'sort': sort,
			   'page': page}
	try:
		response = requests.get(requrl, params = payload)
	except:
		print 'request fail'
		return -1

	# stop if limit reached and return error code
	if response.json().values()[0] == 'limit':
		print 'limit reached'
		return -1

	#add page number it was pulled from
	#count = response.json()['count']
	result = []
	for item in response.json()['recipes']:
		item['page'] = page
		result.append(item)
	
	return result

def f2f_getnextpage(table):
	d=table.find().sort([('page', -1)]).limit(1)
	d=list(d)
	lastpage = d[0]['page']

	q = f2fquery(page = lastpage + 1)
	if q != -1:
		tab.insert(q)
	else:
		return -1

	return

def f2f_getall():
	#$ sudo mongod
	# requires running mongodb sever
	client = MongoClient()
	# Initiate Database
	db = client['f2f']
	# Initiate Table
	tab = db['recipes']

	result = 0
	i = 0
	while result != -1:
		i += 1
		result = f2f_getnextpage(table)
		if i % 10 == 0:
			print 'Queries: %d, DB size: %d' % (i, table.count())

#yummly


#Safeway
#get data
pages = []
for page in xrange(1,8):
	url = 'http://plan.safeway.com/Circular/San-Francisco-145-Jackson-St-/0C2574301/Weekly/2/%d' % page
	z = requests.get(url).content
	pages.append(z)

products = {'price':list(),
			'brand':list(),
			'title':list()}
price = []
brand = []
title = []

#pnum = 0
pricetable = []

for pnum, page in enumerate(pages, 1):
	#inum = 0
	#pnum +=1
	print 'page ', pnum
	soup = BeautifulSoup(page)
	items = soup.findAll('div', attrs={'class':'tooltip'})
	for inum, item in enumerate(items, 1):
		#inum += 1
		print 'item ', inum
		if len(item) > 3:
			# price.append(item.find('p', attrs={'class':'itemPrice'}).text)
			# brand.append(item.find('p', attrs={'class':'itemBrand'}).text)
			# title.append(item.find('p', attrs={'class':'itemTitle'}).text)
			# products['price'] = products['price'].append(price)
			# products['brand'] = products['brand'].append(brand)
			# products['title'] = products['title'].append(title)
			pricetable.append([
				pnum,
				inum,
				item.find('p', attrs={'class':'itemPrice'}).text,
				item.find('p', attrs={'class':'itemBrand'}).text,
				item.find('p', attrs={'class':'itemTitle'}).text])
			
pricetable = pd.DataFrame(pricetable, columns = ['pagenum', 'itemnum',
												 'price',
												 'brand',
												 'title'])




