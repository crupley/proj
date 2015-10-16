
# Personal Grocer

Weekly meal planner using sale data and recipe recommendation:

Store flier > cost-effective, nutritionally complete recipe selection > grocery list


## Parts

* Local store sale scraping
	* safeway: looks easy enough
	* whole foods: same
* recipes:
	* [food2fork](http://food2fork.com/about/api) - api, 500 calls/day, 30 records per call (15k/day)
	* [yummly](https://developer.yummly.com/) - api, student, 30,000 calls lifetime.
* nutrition:
	* [usda](http://ndb.nal.usda.gov/ndb/doc/index) - ~9000 foods, requires data.gov API key
	* RDA


## Technical skills

* web scraping
* database creation/management/usage
* recommender
* crazy combinatorics problem
* matching names/descriptions