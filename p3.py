# playing youtube video and save  images in computer
import cv2
import pafy
url = 'https://www.youtube.com/watch?v=clkPZY9CPX0'
myvid = pafy.new(url)
data = myvid.getbest(preftype="mp4")
cap = cv2.VideoCapture()
cap.open(data.url)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    cv2.imwrite(f'img/p{count}.jpg', frame)
    print(f'img/p{count}.jpg saved successfully')

    count = count+1
    if cv2.waitKey(25) == ord('q'):
        break
cap.release()

cv2.destroyAllWindows
