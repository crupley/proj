


from pymongo import MongoClient
import requests

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

def f2f_getall(table):
	result = 0
	i = 0
	while result != -1:
		i += 1
		result = f2f_getnextpage(table)
		if i % 10 == 0:
			print 'Queries: %d, DB size: %d' % (i, table.count())



#$ sudo mongod
# requires running mongodb sever
client = MongoClient()
# Initiate Database
db = client['f2f']
# Initiate Table
tab = db['recipes']


'''
tab.insert(c['recipes'])


d=tab.aggregate([{'$group':{'_id':"$page", 'last': {'$max':1}}}])
d=list(d)

x = -1
d=tab.find().sort([('page', -1)]).limit(1)
d=list(d)
['page']
'''

# for page in xrange(468, 490):
# 	if page % 10 == 0:
# 		print 'Pages pulled: %d, DB size: %d' % (page, tab.count())
# 	q = f2fquery(page=page)
# 	tab.insert(q)
