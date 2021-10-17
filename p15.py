import cv2
import numpy as np


cv2.namedWindow("win")

cap = cv2.VideoCapture(0)


def chess(x):
    pass


cv2.createTrackbar('lh', 'win', 0, 255, chess)
cv2.createTrackbar('ls', 'win', 0, 255, chess)
cv2.createTrackbar('lv', 'win', 0, 255, chess)


cv2.createTrackbar('uh', 'win', 255, 255, chess)
cv2.createTrackbar('us', 'win', 255, 255, chess)
cv2.createTrackbar('uv', 'win', 255, 255, chess)

while cap.isOpened():
    lh = cv2.getTrackbarPos('lh', 'win')
    ls = cv2.getTrackbarPos('ls', 'win')
    lv = cv2.getTrackbarPos('lv', 'win')
    uh = cv2.getTrackbarPos('uh', 'win')
    us = cv2.getTrackbarPos('us', 'win')
    uv = cv2.getTrackbarPos('uv', 'win')
    ret, frame = cap.read()

    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])
    mask = cv2.inRange(frame, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("res", res)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
