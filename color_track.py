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

#Gitted_red
lower =np.array([145,130,160])
upper =np.array([180,255,255])


green = (0, 255, 0)
blue  = (255, 0, 0)
red   = (0, 0, 255)
x=0
y=0
x_colllect =0
y_colllect =0
time =1
current_position =0
current_position_x =0
current_position_y =0

def show_distance (trgt_length,focallength,per_length):
    
    distance=(trgt_length*focallength) / per_length
    
    print (distance)


#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv2.VideoCapture(0)
while True:
    
    arg,img=cap.read() #从摄像头读取图片

 
   # cv2.imshow("img",img)
    

    hsv_frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#将每一帧图片转化HSV空间颜色
    mask = cv2.inRange(hsv_frame,lower,upper)
    cv2.imshow ("mask", mask)
    conts,hier = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#找出边界
    cv2.drawContours(img,conts,-1,blue,2)#画出边框
    dst = cv2.bitwise_and(img,img,mask=mask)#对每一帧进行位与操作，获取追踪图像的颜色
    cv2.imshow ("dst",dst)
    cv2.imshow ("img2",img)

   

    for i in range(0,len(conts)):  
        x, y, w, h = cv2.boundingRect(conts[i])   
        cv2.rectangle(img, (x, y), (x + w, y + h), green, 2) 
        #show_distance (10,20,h)

   
   
   
    check_time =11
    correction_value =5
       
    if time <check_time:
        #print (time)
        x_colllect = x_colllect + x + (w/2)
        y_colllect = y_colllect + y + (h/2)
        # print (x_colllect,x)
        time=time+1
    else :
    # print ("result:")
        if ((x_colllect / check_time) < (current_position_x-correction_value)) or ((x_colllect / check_time) > (current_position_x+correction_value)):
            current_position_x = x_colllect/check_time
            #print (current_position, x_colllect)
        if ((y_colllect / check_time) < (current_position_y-correction_value)) or ((y_colllect / check_time) > (current_position_y+correction_value)):
            current_position_y = y_colllect/check_time
            
            current_position= (current_position_x, current_position_y)

            print (current_position)
            #print ("END:")
        x_colllect = 0
        y_colllect = 0
        time =1

    
  

    key =cv2.waitKey(1) #保持画面的持续。
    if key == ord ("Q"):
        if time <check_time:
            #print (time)
            x_colllect=x_colllect+x
           # print (x_colllect,x)
            time=time+1

        else :
            # print ("result:")
            print (x_colllect/check_time)
            #print ("END:")
            x_colllect = 0
            time =1
            
    elif key == ord ("W"):
        print ("**************************** END X",check_time, "****************************")
        break
        

    cv2.imshow("img",img)


    if key == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif key ==ord("S"):
        #通过s键保存图片，并退出。
        cv2.imwrite("image3.jpg",img)
        cv2.destroyAllWindows()
        break
        
#关闭摄像头
cap.release()
