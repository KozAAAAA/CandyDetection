import cv2
import numpy as np

img = cv2.imread('home.jpg',0)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel1)
div = np.float32(gray)/(close)
res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))