# Picture to calories

## Description

Identify the amount of calories in a meal from a picture.


## Evaluation

1. Asks a good question
	Can we find an easier way to track calorie intake by using pictures?
2. Technically impressive
	Requires image classification mated with calorie database
3. Obvious utility
	Allows simple dietary tracking
4. Wrapping paper
	web app/phone app


## Data needs and availability

* Labeled food image dataset available
	* [PFID](http://pfid.rit.albany.edu/): Pittsburgh fast-food image dataset: 4,500 images of 101 foods.
* food nutrient database
	* database of 7,000 foods available from US agricultural research service
* if necessary, could decompose foods into ingredients from recipe data:
	* recipe information
		* 200,000+ recipes available through api
		* if api limits reached, can resort to scraping

## Risks

* neural network...
* inadequate training data
* difficulty dealing with image background noise
* calibrating meal size in image