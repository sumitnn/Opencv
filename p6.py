# show date,time,height and width in live video
import cv2
import datetime


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.putText(frame, str(datetime.datetime.now()), (10, 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    data = f"width:{int(cap.get(3))} height:{int(cap.get(4))}"

    frame = cv2.putText(frame, data, (70, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imshow("video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
