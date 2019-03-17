import cv2 #loading the opencv library to python code

img = cv2.imread('../samples/flower.jpg')

#print(img)
# #print BGR values in a image

#print(img[100][100]) #print value of 100 row and 100 column

cv2.imshow('WINDOW',img)

#img[100][100]=[255,255,255]

#cv2.imshow('WINDOW',img)

#cv2.rectangle(img,(100,100),(200,200),(0,255,0),2) #whare we draw,position,color,line width

#cv2.imshow('WINDOW',img)

#cv2.circle(img,(150,150),40,(255,0,0),3)
#cv2.imshow("WINDOW",img)
