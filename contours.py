import cv2
import numpy as np


cv2.namedWindow("normal", cv2.WINDOW_NORMAL)
cv2.namedWindow("red", cv2.WINDOW_NORMAL)
cv2.namedWindow("purple", cv2.WINDOW_NORMAL)
cv2.namedWindow("yellow", cv2.WINDOW_NORMAL)
cv2.namedWindow("green", cv2.WINDOW_NORMAL)

cv2.resizeWindow("normal", 500, 500)
cv2.resizeWindow("red", 500, 500)
cv2.resizeWindow("purple", 500, 500)
cv2.resizeWindow("yellow", 500, 500)
cv2.resizeWindow("green", 500, 500)

def get_number_of_objects_in_range(img: cv2.Mat, lower_hsv_limits: list[np.ndarray], upper_hsv_limits: list[np.ndarray]) -> any:
    
    kernel = np.ones((5,5),np.uint8)

    blurred_img = cv2.GaussianBlur(img, (41, 41), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv_img, lower_hsv_limits[0], upper_hsv_limits[0])

    for i in range(len(lower_hsv_limits)):
        temporary_mask = cv2.inRange(hsv_img, lower_hsv_limits[i], upper_hsv_limits[i])
        mask = cv2.bitwise_or(mask, temporary_mask)

    opening_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    dilate_mask = cv2.dilate(opening_mask, kernel , iterations=4)
    contours, _ = cv2.findContours(dilate_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    return len(contours), dilate_mask


img = cv2.imread("data/00.jpg", cv2.IMREAD_COLOR)

lower_red = [np.array([175, 165, 137]), np.array([0, 165, 137])]
upper_red = [np.array([179, 255, 200]), np.array([1, 255, 200])]

lower_purple = [np.array([158,108,24])]
upper_purple = [np.array([173,255,105])]

lower_yellow = [np.array([10,168,199])]
upper_yellow = [np.array([30,255,255])]

lower_green = [np.array([31,140,158])]
upper_green = [np.array([52,255,255])]

red_count, red_display = get_number_of_objects_in_range(img, lower_red, upper_red)
purple_count, purple_display = get_number_of_objects_in_range(img, lower_purple, upper_purple)
yellow_count, yellow_display = get_number_of_objects_in_range(img, lower_yellow, upper_yellow)
green_count, green_display = get_number_of_objects_in_range(img, lower_green, upper_green)

print("red = " + str(red_count))
print("purple = " + str(purple_count))
print("yellow = " + str(yellow_count))
print("green = " + str(green_count))


cv2.imshow("normal", img)
cv2.imshow("red", red_display)
cv2.imshow("purple", purple_display)
cv2.imshow("yellow", yellow_display)
cv2.imshow("green", green_display)


cv2.waitKey(0)
cv2.destroyAllWindows()