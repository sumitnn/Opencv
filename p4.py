# make  video from save  images in computer ANS SHOW ALSO
import cv2
import os

result = cv2.VideoWriter('oggy11.avi',
                         cv2.VideoWriter_fourcc(*'XVID'),
                         20, (int(700), int(600)))

count = 0
while True:
    img = f"img/p{count}.jpg"
    a = cv2.imread(img)

    cv2.imshow('video', a)
    result.write(a)

    count = count+1
    if cv2.waitKey(0) == ord('q'):
        break


cv2.destroyAllWindows
