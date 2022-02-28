"""

""" 
##Imports------------------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt
from process_image import *
import sympy as sy
from numba import njit
# from quantulum import parser

##Main Funktions-----------------------------------

##Other Funktions----------------------------------

def parse_task_data(task_data):
	input_values = {}

	for item in task_data:
		if "∠" in item:
			x = item.index("∠")
			task_data[task_data.index(item)] = item[:x]

	for item in task_data:
		item_l = item.split("=")
		ite = item_l[1].strip()
		if "T" in ite:
			ite_l = ite.split("T")
			num = eval(f"{ite_l[0]}* 10**12")
		elif "G" in ite:
			ite_l = ite.split("G")
			num = eval(f"{ite_l[0]}* 10**9")
		elif "M" in ite:
			ite_l = ite.split("M")
			num = eval(f"{ite_l[0]}* 10**6")
		elif "k" in ite:
			ite_l = ite.split("k")
			num = eval(f"{ite_l[0]}* 10**3")
		elif "m" in ite:
			ite_l = ite.split("m")
			num = eval(f"{ite_l[0]}* 10**(-3)")
		elif "μ" in ite:
			ite_l = ite.split("μ")
			num = eval(f"{ite_l[0]}* 10**(-6)")
		elif "n" in ite:
			ite_l = ite.split("n")
			num = eval(f"{ite_l[0]}* 10**(-9)")
		elif "p" in ite:
			ite_l = ite.split("p")
			num = eval(f"{ite_l[0]}* 10**(-12)")
		else:
			string_int = ""
			for i in ite:
				if i == ".":
					string_int += "."
				elif i.isdigit():
					string_int += i
				else:
					pass
			num = float(string_int)

		input_values[item_l[0].strip()] = num
	return input_values


##Other--------------------------------------------

#schould come from scrapint
task_data = ['UQ1=16V∠0°', ' R1=82Ω', ' L1=8.2mH', ' C1=820nF', ' f=368Hz']
input_field_names = ['Z', 'input', '∠', 'input', 'I', 'input', '∠', 'input', 'U', 'R', '1', 'input', '∠', 'input', 'U', 'L', '1', 'input', '∠', 'input', 'U', 'C', '1', 'input', '∠', 'input']
task_image = cv2.imread("vorlagebilder/bilder-aller-aufgaben/18.png")

with open("bild-template-datenbank.json","r") as file:
	template_data = json.load(file)

print(parse_task_data(task_data))
# print(parser.parse(task_data[0]))
# print(parser.parse('I want 2 liters of wine'))


#go_through_image(task_image, search_image)


found_pixels = np.full(task_image.shape[0:2], False)

raw_data, found_pixels = find_bauteile_und_co(task_image, found_pixels, template_data["bauteile"])


print(raw_data)

print("--------")

found_pixels_image = np.full(task_image.shape,0)

for y in range(0,task_image.shape[0]):
	for x in range(0,task_image.shape[1]):

		if found_pixels[y,x] == True:
			found_pixels_image[y,x] = np.array([0,255,0])
		# elif np.all(task_image[y,x] == 0):
		# 	found_pixels_image[y,x] = np.array([0,255,0])

		else:
			found_pixels_image[y,x] = np.array([255,255,255])



plt.imshow(found_pixels_image) #find_bauteile_und_co(task_image))
plt.show()




