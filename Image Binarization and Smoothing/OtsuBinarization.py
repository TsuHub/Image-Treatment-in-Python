import cv2
import numpy as np

img = cv2.imread("images/Placa 2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur

(T, bin) = cv2. threshold (suave, 160, 255, cv2.THRESH_BINARY)

resultado = np.vstack([np.hstack([bin])])

cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

cv2.imwrite("output/Placa 2-BINARIZADO.png", resultado)
