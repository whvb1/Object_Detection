import cv2
import sys
import numpy as np

cap = cv2.VideoCapture('Blackdot.avi')
# height of the fram
height = int(cap.get(4))
print("Height: "+str(height))
# width of the frameQ
width = int(cap.get(3))
print("Width: "+str(width))
Vals = []

while(True):
    ret, img = cap.read()
    gimg = cv2.imread(img, 0)
    cv2.imshow("color",img)
    for y in range(1,height):
        #sys.stdout.write("Row"+str(y)+": ")
        for x in range (0,width-1):
            px = gimg[y,x]
            up = gimg[y-1,x]
            right = gimg[y,x+1]
            if(abs(px-up)<100 or abs(px-right)<100):
                sys.stdout.write(".")
            else:
                img[y,x] = [0,0,255]
                Vals.append([x,y])
            #if(x == width-2):
            #    print(px)
            #else:
            #    sys.stdout.write(str(px))
    sumx = 0
    sumy = 0
    print Vals
    for i in range (0, len(Vals)):
        ptx,pty = Vals[i]
        sumx += ptx
        sumy += pty

    centerX,centerY = (sumx)/len(Vals), (sumy)/len(Vals)
    cv2.circle(img, (centerX,centerY), 4, (0, 0, 255), -1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
