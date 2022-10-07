import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("butterfly.jpeg")
cv.imshow("Fluture galben",img)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread("butterfly.jpeg",cv.IMREAD_GRAYSCALE)
cv.imshow("Fluture gray",img)
cv.waitKey(0)
cv.destroyAllWindows()

H, W = img.shape
print(H,W)

img = cv.resize(img,(100, 100))
H, W = img.shape
print(H,W)
cv.imshow("Fluture gray redimensionat",img)
cv.waitKey(0)
cv.destroyAllWindows()