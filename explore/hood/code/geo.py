
import numpy as np

REARTH = 3959 * 5280 # miles to feet

def make_geo_grid(start, nsrange, ewrange):
	'''
	Makes a grid of latitude, longitude tuples stepped according to 
	north-south and east-west ranges.
	INPUT
		start: (latitude, longitude) tuple of starting point; tuple of float
		nsrange: locations of grid lines relative to start, in feet; list
		ewrange: locations of grid lines relative to start, in feet; list
	RETURNS
		array of lat,lon tuples spaced according to grid
	'''


	startlat, startlon = start
	nsgrid, ewgrid = np.meshgrid(nsrange, ewrange)
	latgrid, longrid = distance_to_angle(start, nsgrid, ewgrid)



	return np.vstack(latgrid.ravel(), longrid.ravel()).T



def distance_to_angle(start, ns, ew):
	'''
	convert distance along surface of earth to lat/lon change
	'''

	lat, lon = start
	lat = deg_to_rad(lat)
	lon = deg_to_rad(lon)

	dlat = ns / float(REARTH)
	dlon = ew / float(REARTH) / np.cos(lat)

	return (rad_to_deg(dlat), rad_to_deg(dlon))


def deg_to_rad(a):
	return a * np.pi / 180

def rad_to_deg(a):
	return a * 180 / np.pi


if __name__ == '__main__':
	citycenter = 	(37.77, -122.454)
	stepsize = 500 #feet
	nsrange = np.arange(-3.5*5280, 3.5*5280, stepsize)
	ewrange = nsrange[:]
	make_geo_grid(citycenter, nsrange, ewrange)