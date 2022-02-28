import numpy as np
import cv2
import matplotlib.pyplot as plt

# method = cv2.TM_SQDIFF_NORMED
method = cv2.TM_CCORR_NORMED
# method = cv2.TM_CCOEFF_NORMED

threshold = 0.9991



buchstabe = cv2.imread(("kondensator.png"))
bild = cv2.imread("beispiel1.png")



result = cv2.matchTemplate(buchstabe, bild, method)

result_cords_x,result_cords_y = np.where(result >= threshold)

for i in range(0,len(result_cords_x)):
	x = result_cords_x[i]
	y = result_cords_y[i]
	
	cv2.rectangle(bild, (y,x),(y + buchstabe.shape[1],x+buchstabe.shape[0]),(0,0,255),1)

	print("found")

print(result_cords_x,result_cords_y)






# Display the original image with the rectangle around the match.
plt.imshow(bild)
plt.show()


##Funktions---------------------------------------------------------------
