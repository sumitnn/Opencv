import cv2
import numpy as np


img = cv2.imread("Data/color_balls.jpg")
cv2.namedWindow("win")


def chess(x):
    pass


cv2.createTrackbar('lh', 'win', 0, 255, chess)
cv2.createTrackbar('ls', 'win', 0, 255, chess)
cv2.createTrackbar('lv', 'win', 0, 255, chess)


cv2.createTrackbar('uh', 'win', 255, 255, chess)
cv2.createTrackbar('us', 'win', 255, 255, chess)
cv2.createTrackbar('uv', 'win', 255, 255, chess)

while True:
    lh = cv2.getTrackbarPos('lh', 'win')
    ls = cv2.getTrackbarPos('ls', 'win')
    lv = cv2.getTrackbarPos('lv', 'win')
    uh = cv2.getTrackbarPos('uh', 'win')
    us = cv2.getTrackbarPos('us', 'win')
    uv = cv2.getTrackbarPos('uv', 'win')
    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])
    mask = cv2.inRange(img, lower, upper)

    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("res", res)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
