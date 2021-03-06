import numpy as np
import cv2
from cv2 import cv2
import imutils
#Green
#lower = np.array([35,43,46])
#upper = np.array([77,255,255])

#RED
#lower = np.array([156,43,46])
#upper = np.array([180,255,255])

#YELLOW
#lower = np.array([26,43,46])
#upper = np.array([34,255,255])

#BLUE
lower = np.array([78,43,46])
upper = np.array([124,255,255])

green = (0, 255, 0)
blue  = (255, 0, 0)
red   = (0, 0, 255)



#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv2.VideoCapture(0)



while True:
    
    sucess,img=cap.read() #从摄像头读取图片

 
   # cv2.imshow("img",img)
    

    hsv_frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#将每一帧图片转化HSV空间颜色
    mask = cv2.inRange(hsv_frame,lower,upper)
    #cv2.imshow ("mask", mask)
    conts,hier = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#找出边界
    cv2.drawContours(img,conts,-1,blue,1)#画出边框
    dst = cv2.bitwise_and(img,img,mask=mask)#对每一帧进行位与操作，获取追踪图像的颜色
   # cv2.imshow ("dst",dst)
    #cv2.imshow ("img2",img)

    for i in range(0,len(conts)):  
        x, y, w, h = cv2.boundingRect(conts[i])   
        cv2.rectangle(img, (x,y), (x+w,y+h), (153,153,0), 2) 

    cv2.imshow("img",img)
    #print (conts)
    cv2.imwrite("image2.jpg",img)











    k=cv2.waitKey(1) #保持画面的持续。
    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):
        #通过s键保存图片，并退出。
        cv2.imwrite("image2.jpg",img)
        cv2.destroyAllWindows()
        break
#关闭摄像头
cap.release()
