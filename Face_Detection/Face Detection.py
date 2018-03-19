import cv2
print("Imported CV2")
import serial
print("Imported Serial")
from time import gmtime, strftime
print("Imported GMTIME")
import time
print("Imported TIME")
print('Initialization...')
#video stuff
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def Lock(x, y, w, h):
    Lx, Ly, Lw, Lh= x-w, y-h, x+w+w, y+h+h
    return Lx, Ly, Lw, Lh

cap = cv2.VideoCapture(0)

print("RUNNING")

# height of the fram
height = int(cap.get(4))
# width of the frame
width = int(cap.get(3))
# center of frame
centerX,centerY=width/2,height/2
# size of crosshair
size = 20


# serial stuff

#aD = serial.Serial('COM3',9600)

# px to degree
#------
sensitivityX, sensitivityY = 30.1,30.1

#Face Lock
Lx,Ly,Lw,Lh = 0,0,width,height


while True:
    print("...")
    ret,image=cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.line(gray, (centerX, centerY-size), (centerX, centerY+size),(255,255,255),3)
    cv2.line(gray, (centerX-size, centerY), (centerX+size, centerY),(255,255,255),3)

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    eyes = eye_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        if(x>Lx and y>Ly and (x+w)<Lw and (y+h)<Lh):
            Lx, Ly, Lw, Lh = Lock(x, y, w, h)
            cv2.rectangle(gray,(Lx,Ly),(Lw,Lh),(255,255,255),4)
            ####  rectangle ( on what?, top left coordinate, bottom right, color, line width)
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 3)
            cv2.arrowedLine(gray, (centerX, centerY), (x+int(.5*w), y+int(.5*h)),4)
            angleX, angleY = (x+int(.5*w)-centerX)/sensitivityX, (y+int(.5*h)-centerY)/sensitivityY
            print(angleX,angleY)
            angleX = round(angleX,4)
            angleY = round(angleY,4)
            data = str(angleX)+","+str(angleY)
            if(abs(angleX)<1):
                if(abs(angleY)<1):
                    print("Target Acquired")
                else:
                    print("Target in view")
            #else:
                #aD.write(data)
            print(data)

            print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            #print(aD.read_all())
        cv2.imshow("VIDEO_FEED_COLOR",image)
        #plt.imshow('PYPLOT_VIDEO_FEED',cmap=image2,interpolation='bicubic')
        cv2.imshow('VIDEO_FEED_GRAY_FACE', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("COMPLETE")




