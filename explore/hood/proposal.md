# Neighborhood identification and similarity

Chris Rupley

October 26, 2015


## Description

The objective of this project is to independently identify neighborhoods and boundaries in a city based on census data, business data, and other demographic data. This information can then be used, for example,

* by residents who are moving to a new home and want particular neighborhood characteristics; especially if moving to a new city they are unfamiliar with.
* by businesses looking to expand where they can best reach their target customers.
* by government entities to plan events and services.


## Evaluation

1. Asks a good question
	* Can we identify neighborhood boundaries based on functional characteristics and list similar neighborhoods?
2. Technically impressive
	* integration of several potentially disparate data sources
	* clustering, dimensionality reduction, hidden features
	* similarity
	* geo-spatial analysis
4. Wrapping paper
	* web app, interactive maps

## Data needs and availability

A wide range of sources are possible. Some examples:

* US Census data: population, demographics, business, housing, etc., etc.
* yelp api: 25,000 calls/day, up to 40 results/call -> 1M per day
* SF OpenData: Public data from the city of San Francisco. Registered businesses, crime, property value (for San Francisco only)

## Risks

* data integration
* available data too sparse or not localized enough
* choosing the right data to use to make a good prediction; sifting through wealth of available to find most useful data.

## Next Steps

* gather and organize potentially required data
* cluster geographically for one city
* explore relationships

