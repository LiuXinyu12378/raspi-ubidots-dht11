import cv2
import numpy as np
import time

img=cv2.imread('wlw.jpg')
cv2.namedWindow('image_color',cv2.WINDOW_NORMAL)
cv2.putText(img, text="liuxinyu", org=(300, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
cv2.imshow('image_color',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

cv2.putText(img, text="asjlfasdjil", org=(300, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=2, lineType=cv2.LINE_AA, color=(0, 0, 250))
cv2.imshow('image_color',img)
cv2.waitKey(0)
cv2.destroyAllWindows()