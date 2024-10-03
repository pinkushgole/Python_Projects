# pip install opencv-python : image proccesing karna me use hoti hai image color,filtring etc

import cv2

# face detection 
face_cap=cv2.CascadeClassifier("D:/Django/Python/projects1/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")



#  camera open code
 
video_cap=cv2.VideoCapture(0)

while(True):
    ret,video_data=video_cap.read()  # vide capture
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) # videeo bake-white color change
    faces=face_cap.detectMultiScale(  # vaps color me convert  kiya
         col,
         scaleFactor=1.1,
         minNeighbors=5,
         minSize=(30,30),
         flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces: # create box
         cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live",video_data ) # create video fame open
    if cv2.waitKey(10) == ord("a"):
         break

video_cap.release()