import cv2

camera = cv2.VideoCapture(0) #0 default camera

while(True):
    ret,frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("LIVE",frame)
    cv2.imshow("LIVE",gray)
    cv2.waitKey(1) #1 milisecond elay