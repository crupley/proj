
# Notes on neighborhood clustering

## Data


###Have

* crime
	* [https://data.sfgov.org/Public-Safety/SFPD-Incidents-from-1-January-2003/tmnf-yvry] (by district)
* business
	* (registered businesses sf)[https://data.sfgov.org/Economy-and-Community/Registered-Business-Locations-San-Francisco/g8m3-pdis]


###Getting


###Potential

* yelp api
	* (https://www.yelp.com/developers/documentation/v2/overview)
	* 25,000 calls/day, up to 40 results/call -> 1M per day?
* [US Census](http://factfinder.census.gov/faces/nav/jsf/pages/download_center.xhtml)
* [sfdata](data.sfgov.org)
* walkscore
	* requested academic data
	* api: 5,000 requests per day
	* data snaps to lat/long on 500ft. grid
	* San Francisco: 7mi x 7mi -> 70 pts x 70 pts -> **4,900** pts

* property values
	* (sf assessor)[http://propertymap.sfplanning.org/] (okay scrape, from address)
* business $$$, ratings, density(grocery, gas, shop...)
* schools
* demographic
	* income
	* age
	* employment


###SF Open Data, checked
* all tabular data