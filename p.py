# saving live video in local system
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
result = cv2.VideoWriter('live.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (int(cap.get(3)), int(cap.get(4))))
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("live video", frame)
    result.write(frame)
    print(cap.get(3))

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
result.release()
cv2.destroyAllWindows()
