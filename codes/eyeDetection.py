import cv2

camera = cv2.VideoCapture(0) #0 default camera also we can use another video source like films

eye_clsfr = cv2.CascadeClassifier("../haarcascade_eye_tree_eyeglasses.xml")

while(True):
    ret,frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#detect color image as gray

    #below line similar to result = clsfr.predict(test_data)
    faces = eye_clsfr.detectMultiScale(gray)

    #detect eyes
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)

    #cv2.imshow("LIVE",frame)
    cv2.imshow("LIVE",frame)
    #cv2.imshow("LIVE",gray)
    cv2.waitKey(1) #1 milisecond elay