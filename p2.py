# playing youtube video and save  video in computer
import cv2
import pafy
url = 'https://www.youtube.com/watch?v=clkPZY9CPX0'
myvid = pafy.new(url)
data = myvid.getbest(preftype="mp4")
cap = cv2.VideoCapture()
cap.open(data.url)
result = cv2.VideoWriter('oggy.avi',
                         cv2.VideoWriter_fourcc(*'XVID'),
                         20, (int(cap.get(3)), int(cap.get(4))))
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    result.write(frame)
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()
result.release()
cv2.destroyAllWindows
