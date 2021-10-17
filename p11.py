# image blending software
import cv2
import numpy as np
img = np.zeros((600, 600, 3), dtype=np.uint8)
img1 = cv2.imread('Data/hero1.jpg')
img2 = cv2.imread('Data/hero2.jpg')
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))
cv2.namedWindow("win")


def press(x):
    pass


switch = "O to 1"
cv2.createTrackbar(switch, "win", 0, 1, press)
cv2.createTrackbar("a", "win", 1, 100, press)

while True:
    s = cv2.getTrackbarPos(switch, "win")
    a1 = cv2.getTrackbarPos('a', "win")
    a = float(a1/100)

    if s == 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1, 1-a, img2, a, 0)
        cv2.putText(dst, str(a), (20, 50),
                    cv2.FONT_ITALIC, 2, (0, 125, 255), 2)
    cv2.imshow("f", dst)
    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
