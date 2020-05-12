import cv2
import numpy as np
# import matplotlib.pyplot as plot

img = cv2.imread("images/Placa 2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur

resultado = np.vstack([
	np.hstack([suave])
        ])

cv2.imshow("Cinza e Suavizado", resultado)
cv2.waitKey(0)

cv2.imwrite("output/Placa 2-CINZA-SUAVIZADO.png", resultado)
