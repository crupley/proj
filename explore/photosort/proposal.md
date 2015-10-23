# Photosort

Chris Rupley
October 26, 2015

## Description

Automatic organization of photo library featuring,

	* identification of high-quality images based on similarity to other 'good' images as well as other image metrics such as composition, color histogram, and saturation.
	* removal of poor quality images; blurred, too dark/light, etc.
	* sort according to photo location, event, or time period.


## Evaluation

1. Asks a good question
	Can we make it easier to find the best images in a photo library?
2. Technically impressive
	Image featurization, classification, other ML prediction, api, clustering
3. Obvious utility
	Get your best images without sorting through 1,000's
4. Wrapping paper
	image gallery


## Data needs and availability

* lots of images
	* personal collection of good and bad images
* Flickr api
	* source of 'good' training images based on favorited, comments

## Risks

* developing good model
* getting adequate information from training set (can favorites and comments indicate best pictures?)

## Next steps

* Gather image data, metadata, and ratings from Flickr
* Investigate image feature importances