print ("I know I have python downloaded")
import time
print("Successfully imported time")
import cv2
print("Successfully imported cv2")
import numpy as np
print("Successfully imported numpy")
import matplotlib.pyplot as plt
print("Successfully imported matplotlib")
import serial
print("Imported Serial")

def VideoFeed():
    print("Running VideoFeed")
    cap = cv2.VideoCapture(0)
    # height of the fram
    height = int(cap.get(4))
    # width of the frameQ
    width = int(cap.get(3))
    # center of frame
    centX, centY = width / 2, height / 2
    # size of crosshair
    size = 10
    thickness = 1
    scale = 5 # used in edge detection
    scaleY = int(height / scale)
    scaleX = int(width / scale)
    threshold = 100
    sensitivityX = 15
    sensitivityY = 15
    n=0 # serial loop
    #aD = serial.Serial('COM3', 9600)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()


        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.line(frame, (centX, centY - size), (centX, centY + size), (0, 0, 0), thickness)
        cv2.line(frame, (centX - size, centY), (centX + size, centY), (0, 0, 0), thickness)
        # Display the resulting frame
        Vals = []
        #print("Running")
        frame[100, 200] = [0, 0, 255]
        #START edge detection --------------------------------------------
        for y in range(1, scaleY):
            # sys.stdout.write("Row"+str(y)+": ")
            for x in range(0, scaleX - 1):
                # print ("in X loop")
                frame[y*scale,x*scale] = [0,0,255]
                # print ("Intensity: ")
                # print intensity\
                #print(gray[y * scale, x * scale])
                #print(gray[(y - 1) * scale, x * scale])
                #print("Difference =")
                #print(int(gray[y * scale, x * scale]) - int(gray[(y - 1) * scale, x * scale]))
                if (abs(int(gray[y * scale, x * scale]) - int(gray[(y - 1) * scale, x * scale])) > threshold) or (abs(int(gray[y * scale, x * scale]) - int(gray[(y ) * scale, (x+1) * scale])) > threshold):
                    #or (
                    #abs(gray[y * scale, x * scale] - gray[y * scale, (x + 1) * scale]) > threshold):
                    #frame[y * scale, x * scale] = [255, 0, 255]
                    #print("Difference Detected")
                    cv2.circle(gray2, (x*scale, y*scale), 1, (255, 0, 0), -1)# small white circles
                    Vals.append([x * scale, y * scale])
                    #print("No edge at: ")
                    #print(x,y)


                # if(x == width-2):
                #    print(px)
                # else:
                #    sys.stdout.write(str(px))
        sumx= 0
        sumy= 0
        #print("len(Vals)")
        #print (len(Vals))
        centerX = centX
        centerY = centY
        if(len(Vals)>0):
            #print(Vals)
            for i in range(0, len(Vals)):
                ptx, pty = Vals[i]
                sumx += ptx
                sumy += pty

            centerX, centerY = (sumx) / len(Vals), (sumy) / len(Vals)

        cv2.circle(gray2, (centerX, centerY), 10, (0, 0, 255), -1)
        cv2.line(gray2, (centerX, centerY - size), (centerX, centerY + size), (255,255,255), thickness)
        cv2.line(gray2, (centerX - size, centerY), (centerX + size, centerY), (255,255,255), thickness)

        #END edge and center detection ---------------------------------------------------------


        #START sending data to arduino ---------------------------------------------------------
        cv2.arrowedLine(gray2, (centX, centY), (centerX, centerY), 4)
        angleX, angleY = (centerX - centX) / sensitivityX, (centerY - centY) / sensitivityY
        #print(angleX, angleY)
        angleX = round(angleX, 4)
        angleY = round(angleY, 4)
        data = str(angleX) + "," + str(angleY)
        # if(abs(angleX)<1):
        #    if(abs(angleY)<1):
        #        print("Target Acquired")
        #    else:
        #        print("Target in view")
        #n += 1
        #if(n==15):
            #aD.write(data)  # sending the data to the Arduino
        #    n=0



        #print("SENT DATA")

        #print(data)
        #END sending data to arduino ---------------------------------------------------------


        cv2.imshow('edges', gray2)
        cv2.imshow('color', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
img = cv2.imread('2017-18 Classes.PNG',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('2017-18 Classes.PNG',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(time.daylight)
VideoFeed()