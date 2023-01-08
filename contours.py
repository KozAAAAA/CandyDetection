import cv2
import numpy as np


img = cv2.imread("data/26.jpg", cv2.IMREAD_COLOR)
blurred_img = cv2.GaussianBlur(img, (41, 41), 0)
hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)

lower_red_mask = np.array([173, 91, 100])
upper_red_mask =np.array([179, 255, 255])
lower_purple_mask = np.array([140,0,0])
upper_purple_mask =np.array([173,255,103])

lower_yellow_mask = np.array([10,201,119])
upper_yellow_mask =np.array([30,255,255])

lower_green_mask = np.array([31,188,119])
upper_green_mask =np.array([52,255,255])

red_mask = cv2.inRange(hsv_img, lower_red_mask, upper_red_mask)
purple_mask = cv2.inRange(hsv_img, lower_purple_mask, upper_purple_mask)
yellow_mask = cv2.inRange(hsv_img, lower_yellow_mask, upper_yellow_mask)
green_mask = cv2.inRange(hsv_img, lower_green_mask, upper_green_mask)

kernel = np.ones((5,5),np.uint8)

# closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel) instead!!!! of dilate

# red_mask = cv2.dilate(red_mask, kernel , iterations=1)
# purple_mask = cv2.dilate(purple_mask, kernel , iterations=1)
# yellow_mask = cv2.dilate(yellow_mask, kernel , iterations=1)
# green_mask = cv2.dilate(green_mask, kernel , iterations=1)

red_opening = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations=3)
purple_opening = cv2.morphologyEx(purple_mask, cv2.MORPH_OPEN, kernel, iterations=3)
yellow_opening = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel, iterations=3)
green_opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=3)

red_contours, _ = cv2.findContours(red_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
purple_contours, _ = cv2.findContours(purple_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
yellow_contours, _ = cv2.findContours(yellow_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
green_contours, _ = cv2.findContours(green_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("red = " + str(len(red_contours)))
print("purple = " + str(len(purple_contours)))
print("yellow = " + str(len(yellow_contours)))
print("green = " + str(len(green_contours)))

cv2.namedWindow("red", cv2.WINDOW_NORMAL)
cv2.namedWindow("normal", cv2.WINDOW_NORMAL)

cv2.resizeWindow("normal", 500, 500)
cv2.resizeWindow("red", 500, 500)

cv2.imshow("normal", img)
cv2.imshow("red", red_opening)

cv2.waitKey(0)
cv2.destroyAllWindows()