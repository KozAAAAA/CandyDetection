import cv2
import numpy as np

def empty(i):
    pass

path = "data/06.jpg"
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)

img = cv2.imread(path)

def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")
    
    val_add = cv2.getTrackbarPos("Val Add", "TrackedBars")
    sat_add = cv2.getTrackbarPos("Sat Add", "TrackedBars")

    val_sub = cv2.getTrackbarPos("Val Sub", "TrackedBars")
    sat_sub = cv2.getTrackbarPos("Sat Sub", "TrackedBars")


    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    blurred_img = cv2.GaussianBlur(img, (41, 41), 0)
    img_hsv = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)
    imgMASK = cv2.inRange(img_hsv, lower, upper)

    cv2.namedWindow("Output1", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Output1", 500, 500)
    cv2.resizeWindow("Mask", 500, 500)

    cv2.imshow("Output1", img)
    cv2.imshow("Mask", imgMASK)


cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Add", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Add", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Sub", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Sub", "TrackedBars", 0, 255, on_trackbar)



# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv2.waitKey()