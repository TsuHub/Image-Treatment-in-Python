import cv2
import numpy as np
# import matplotlib.pyplot as plot
img = cv2.imread("images/Placa 2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Cinza", img)
cv2.waitKey(0)

cv2.imwrite("output/Placa 2-CINZA.png", img)
