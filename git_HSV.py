import numpy as np
import cv2
from cv2 import cv2


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
#lower = np.array([78,43,46])
#upper = np.array([124,255,255])


     



def nothing(x):
    pass
def createbars():
    """
    实现创建六个滑块的作用，分别控制H、S、V的最高值与最低值
    """
    cv2.createTrackbar("H_l","image",0,180,nothing)
    cv2.createTrackbar("H_h","image",0,180,nothing)
    cv2.createTrackbar("S_l","image",0,255,nothing)
    cv2.createTrackbar("S_h","image",0,255,nothing)
    cv2.createTrackbar("V_l","image",0,255,nothing)
    cv2.createTrackbar("V_h","image",0,255,nothing)
cv2.namedWindow("image")
createbars()#创建六个滑块


lower = np.array([0,0,0])#设置初始值
upper = np.array([0,0,0])

cap=cv2.VideoCapture(0)


while True:

    flat,newImg = cap.read()
        # the picuture info is in the "newImg"

    hsv_frame = cv2.cvtColor(newImg,cv2.COLOR_BGR2HSV)#将图片由BGR颜色空间转化成HSV空间，HSV可以更好地分割颜色图形
    lower[0]=cv2.getTrackbarPos("H_l","image")#获取"H_l"滑块的实时值
    upper[0]=cv2.getTrackbarPos("H_h","image")#获取"H_h"滑块的实时值
    lower[1]=cv2.getTrackbarPos("S_l","image")
    upper[1]=cv2.getTrackbarPos("S_h","image")
    lower[2]=cv2.getTrackbarPos("V_l","image")
    upper[2]=cv2.getTrackbarPos("V_h","image")
    
    mask = cv2.inRange(hsv_frame,lower,upper)#cv2.inrange()函数通过设定的最低、最高阈值获得图像的掩膜
    cv2.imshow("imge",newImg)
    cv2.imshow("image",mask)



    key =cv2.waitKey(1) #保持画面的持续。
            
    #if cv2.waitKey(1)&0xff == 27newImg
    if key ==27:    
        cv2.destroyAllWindows()
        break
cap.release()