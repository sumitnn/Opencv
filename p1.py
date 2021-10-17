# screen recorder
import cv2
import pyautogui as p
import numpy as np

data = p.size()

result = cv2.VideoWriter('screen.avi',
                         cv2.VideoWriter_fourcc(*'XVID'),
                         20, data)
# create recording module
cv2.namedWindow("recoder", cv2.WINDOW_NORMAL)
# Resize the window
cv2.resizeWindow("recoder", (600, 400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    result.write(f)
    cv2.imshow("recoder", f)
    if cv2.waitKey(1) == ord('q'):
        break

result.release()
cv2.destroyAllWindows()
