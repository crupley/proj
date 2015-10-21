
# Personal Grocer

Weekly meal planner using sale data and recipe recommendation:

Store flier > cost-effective, nutritionally complete recipe selection > grocery list


## Parts

* Local store sale scraping
	* safeway: looks easy enough
	* whole foods: same
* recipes:
	* [food2fork](http://food2fork.com/about/api) - api, 500 calls/day, 30 records per call (15k/day)
		* 'over 200,000 recipes'
	* [yummly](https://developer.yummly.com/) - api, student, 30,000 calls lifetime.
* nutrition:
	* [usda](http://ndb.nal.usda.gov/ndb/doc/index) - ~9000 foods, requires data.gov API key
		* dl from https://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR/SR28/dnload/sr28asc.zip
	* RDA
		dl from http://www.cnpp.usda.gov/sites/default/files/dietary_guidelines_for_americans/PolicyDoc.pdf

## Challenges

* integration
* nutrition combinatorics
* store prices, non-sale

## Technical skills

* web scraping
* database creation/management/usage
* recommender
* crazy combinatorics problem
* matching names/descriptions

## 4 Questions

1. Ask a good question - can meal planning be automated, cheap, and good
2. Technically impressive - many DS skills, though not much ML
3. Obvious utility - save $, time. Health
4. wrapping / UI - many possibilities

## Competition

* [http://www.foodplannerapp.com/](http://www.foodplannerapp.com/) - import and edit own recipes, grocery list, meal plans, (inventory?) - **no health / sale info**
* [cookinglight](http://www.cookinglight.com/weeknight-meal-planner) - very slick drag-and-drop image planner