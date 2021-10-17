import cv2
import numpy as np

# create black blank image
img = np.zeros([512, 512, 3], dtype=np.uint8)*255
# Here line accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.line(img, (0, 0), (200, 200), (154, 92, 424), 3)  # color format BGR

# arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (0, 125), (255, 255), (255, 0, 125), 2)

# Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), -1)

#circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), 3)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
