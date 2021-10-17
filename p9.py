
# region of interest
import cv2

img = cv2.imread('data/hero2.jpg')
img = cv2.resize(img, (800, 800))
# 564,133,610,218
# 85,46

roi = img[133:218, 564:610]
img[133:218, 518:564] = roi
img[133:218, 609:655] = roi
img[133:218, 654:700] = roi
img[133:218, 700:746] = roi

cv2.imshow("roi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
