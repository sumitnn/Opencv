# blending
import cv2

img = cv2.imread('Data/hero1.jpg')
img1 = cv2.imread('Data/hero2.jpg')
img = cv2.resize(img, (500, 500))
img1 = cv2.resize(img1, (500, 500))
cv2.imshow("first", img)
cv2.imshow("second", img1)
default = cv2.add(img, img1)
cv2.imshow("default", default)
a = cv2.addWeighted(img, 0.7, img1, 0.3, 0)
cv2.imshow("addweight", a)
cv2.waitKey(0)
cv2.destroyAllWindows()
