
# Notes on neighborhood clustering

## Data


###Have

* crime
	* [https://data.sfgov.org/Public-Safety/SFPD-Incidents-from-1-January-2003/tmnf-yvry] (by district)
		* 107 MB

* business
	* (registered businesses sf)[https://data.sfgov.org/Economy-and-Community/Registered-Business-Locations-San-Francisco/g8m3-pdis]
		* by address
		* 38 MB
* [yelp dataset](https://www.yelp.com/dataset_challenge/dataset)
	* business lat/lon, reviews, users
	* only select cities
	* 575 MB (zipped)
* address to lat lon
	* (http://geocoder.us/)
		* url request -> scrape
	* [US TIGER/line](http://www.census.gov/geo/maps-data/data/tiger.html)(tlgdb)
		* CA
		* address lookup database
		* 219 MB (zipped)
* population density
	* [Gridded population of the world](http://sedac.ciesin.columbia.edu/data/set/gpw-v3-population-density) (usa_gpwv)
		* 2.5 arc-minute bins

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
	* [sf assessor](http://propertymap.sfplanning.org/ )(okay scrape, from address)
* business $$$, ratings, density(grocery, gas, shop...)
* schools
* demographic
	* income
	* age
	* employment
* crime
	* [spotcrime](http://www.spotcrime.com/ca/san+francisco) (scrapable, single table on page, ~3 days) crime type by address
	* [crimereports](https://www.crimereports.com/)
		* scrapable; tables
		* 6 months, crime name, address, date; 1 month at a time
* address to lat lon



###SF Open Data, checked
* all tabular data


###Ref

[spatial cluster analysis](https://books.google.com/books?hl=en&lr=&id=4iqX4926x40C&oi=fnd&pg=PA395&dq=geographic+cluster+boundaries&ots=XHZIU6vDXB&sig=r-e74fc7v0jVtuNcz_gb5_xfB7k#v=onepage&q=geographic%20cluster%20boundaries&f=false) - google books