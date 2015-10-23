# Personal diet manager

Chris Rupley
October 26, 2015


## Description

The goal of the project is to provide personalized meal planning recommendations with some or all of the following features,

* Meeting an individual's recommended or desired nutritional intake.
* Meeting budget needs, perhaps incorporating weekly supermarket sale information.
* Minimizing food waste by planning around food already on hand or about to spoil

## Evaluation

1. Asks a good question
	Can we eat a more healthful diet for less time, money, and waste?
2. Technically impressive
	Requires web scraping and api data access, recipe recommendation, and likely some sort of matrix decomposition for nutrient matching
3. Obvious utility
	saves money, saves time
4. Wrapping paper
	interactive web app, recipe images

## Data needs and availability
	* recipe information
		* 200,000+ recipes available through api (Food2Fork and Yummly)
		* if api limits too restrictive, can resort to scraping
	* recommended dietary intake
		* document available from USDA
	* food nutrient database
		* database of 7,000 foods available from US agricultural research service
	* food prices
		* weekly ad prices can be scraped from store websites: Safeway, Whole Foods...
		* average standard food prices available from USDA

## Risks

* product will not be differentiable from products already available
* problems with obtaining recipe data
* problems with scraping sale price data
* matching descriptions and formats among many different data sources

## Next Steps

* collect and organize all data
* link all data sources with appropriate keys
* establish approach for nutrition match and recommedation