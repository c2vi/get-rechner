import numpy as np
import cv2


search_image = cv2.imread("1.png")

arr = search_image.reshape((search_image.shape[0], -1), order='F')



for a,b in zip([1,2,3,4,5],[6,7,8,9,10]):
	print(a)
	print(b)