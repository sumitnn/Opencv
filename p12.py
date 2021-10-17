import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (150, 100), (200, 250), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (10, 10), (170, 190), (255, 255, 255), -1)

ba = cv2.bitwise_and(img1, img2)
# bo = cv2.bitwise_or(img1, img2)
bo = cv2.bitwise_not(img1)

cv2.imshow('1', img1)
cv2.imshow('2', img2)
# cv2.imshow('ba', ba)
cv2.imshow('bo', bo)
cv2.waitKey(0)
cv2.destroyAllWindows()
