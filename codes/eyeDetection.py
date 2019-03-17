import cv2

camera = cv2.VideoCapture(0) #0 default camera

while(True):
    ret,frame = camera.read()
    cv2.imshow("LIVE")