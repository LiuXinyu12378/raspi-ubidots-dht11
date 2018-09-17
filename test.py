from ubidots import ApiClient
import time
import random
import RPi.GPIO as GPIO
import turtle
from dht11 import dht11
import cv2
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

aaa=0

img=cv2.imread('wlw.jpg',cv2.IMREAD_COLOR)
cv2.namedWindow('区块链技术',cv2.WINDOW_NORMAL)
cv2.putText(img, text="0", org=(300, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
cv2.putText(img, text="0", org=(300, 280), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
cv2.putText(img, text="don't know", org=(300, 360), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
cv2.imshow('区块链技术',img)
cv2.waitKey(10)

api = ApiClient(token='A1E-J1RzJt3Qx5MndvnmIU6aC9eETo5pwt')
global aaa
try:
    temperature=api.get_variable("5b952ebac03f970dbd2dbdf4")
    humidity=api.get_variable("5b95e859c03f9754b1cf9ea8")
    switch=api.get_variable("5b95416ac03f972336fb066a")

except:
    print("Couldn't connect to the API!!")
while(1):
    img2=cv2.imread('wlw.jpg',cv2.IMREAD_COLOR)
    try:
        
        aaa=dht11()
        temperature.save_value({'value':aaa[0]})
        humidity.save_value({'value':aaa[1]})
        
    except:
        print("error!!")
##    turtle.clearscreen()
##    turtle.write("temperature:",move=True,align='left',font=('Arial',40,'normal'))
##    turtle.goto(0,50)
##    turtle.write("humidity   :",move=True,align='left',font=('Arial',40,'normal'))
    try:
        last_value=switch.get_values(1)
    except:
        print("error!")
    print(last_value[0]['value'])
    if(int(last_value[0]['value'])==0):
        GPIO.output(17,GPIO.LOW)
        cv2.putText(img2, text="off", org=(300, 360), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
    if(int(last_value[0]['value'])==1):
        GPIO.output(17,GPIO.HIGH)
        cv2.putText(img2, text="on", org=(300, 360), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
    cv2.putText(img2, text=str(aaa[0]), org=(300, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
    cv2.putText(img2, text=str(aaa[1]), org=(300, 280), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))   
    cv2.imshow('区块链技术',img2)
    cv2.waitKey(10)