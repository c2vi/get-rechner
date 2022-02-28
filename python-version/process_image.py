

##Imports------------------------------------------
from time import time
from os import path
from numba import njit
import matplotlib.pyplot as plt
import numpy as np
import cv2
import json


##Main Funktions----------------------------------------

def find_bauteile_und_co(task_image, found_pixels, bauteil_data):
	"""
		
	"""
	
	#configs for the cv2 altorithm
	threshold = 0.9991
	# method = cv2.TM_SQDIFF_NORMED
	method = cv2.TM_CCORR_NORMED
	# method = cv2.TM_CCOEFF_NORMED
	path_to_bauteil_templates = "./vorlagebilder/bauteile"


	return_data = {}

	for bauteil_name in bauteil_data:

		bauteil_image = cv2.imread(path.join(path_to_bauteil_templates, bauteil_data[bauteil_name]["filename"]))
		result = cv2.matchTemplate(task_image, bauteil_image, method)
		result_cords_y,result_cords_x = np.where(result >= threshold)
		found_bauteile = list(zip(result_cords_y.tolist(),result_cords_x.tolist()))
		return_data[bauteil_name] = found_bauteile

		#this for loop is only used, for setting the found pixels
		for found_bauteil_y,found_bauteil_x in found_bauteile:
			found_pixels[found_bauteil_y:found_bauteil_y + bauteil_data[bauteil_name]["size"][0] , found_bauteil_x:found_bauteil_x + bauteil_data[bauteil_name]["size"][1]] = True

	return(return_data, found_pixels)



def find_beschriftungen(task_image, beschriftungs_data):
	"""

	"""

	pass


##Other Funktions----------------------------------------

@njit #to make this function execute faster
def image_found(image_to_search_in,image_to_search) -> bool:
	"""
	Basically jsut checks if image_to_search_in and image_to_search are the same
	- but white pixels on image_to_search are ignored.
	  - meaning: if a pixel on the image_to_search is white it does not matter what colour the pixel on image_to_search_in is


	"""

	if image_to_search_in.shape != image_to_search.shape:
		return False

	for row_search_in, row_search in zip(image_to_search_in,image_to_search):
		for pixel_search_in, pixel_search in zip(row_search_in,row_search):

			pixel_white = np.all(pixel_search == 255)

				
			if (not np.all(pixel_search == pixel_search_in)) and not pixel_white:
				return False

	return True


@njit #to make this function execute faster
def go_through_image(task_image ,search_image)-> None:
	"""
	goes through every pixel of task_image and checks for the search_image using the image_found function
	"""

	search_image_y = search_image.shape[0]
	search_image_x = search_image.shape[1]

	for y_index in range(0,task_image.shape[0]):
		for x_index in range(0,task_image.shape[1]):
			array_to_compare = task_image[y_index:y_index + search_image_y , x_index:x_index + search_image_x]
			
			#this if statement checks if the array_to_compare is compeltely white, and if it is.....we skip the image found function to make everything faster. hopefully.
			if not (np.all((array_to_compare == 255) | (array_to_compare == 0))):
				if image_found(array_to_compare,search_image):
					print("found")


def get_center(cords,size):
	"""

	size list): [y,x]
	cords (list): [sizey,sizex]
	"""
	
	center_cords = []
	center_cords.append(cords[0]+cords)

	return center_cords

def group_Beschriftungen():
	pass


# result = find_bauteile_und_co()

# print(result[0]);