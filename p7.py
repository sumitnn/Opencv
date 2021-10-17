# mouse event on black screen
import cv2
import numpy as np


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img, "left click", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow("win", img)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.putText(img, "right click", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow("win", img)


img = np.zeros((512, 512, 3), dtype=np.uint8)*255
cv2.imshow('win', img)
cv2.setMouseCallback("win", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
