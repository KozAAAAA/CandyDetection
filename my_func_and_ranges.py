import cv2
import numpy as np

lower_red = [np.array([175, 165, 120]), np.array([0, 165, 120])]
upper_red = [np.array([179, 255, 200]), np.array([1, 255, 200])]

lower_purple = [np.array([158,108,24])]
upper_purple = [np.array([173,255,105])]

lower_yellow = [np.array([10,168,199])]
upper_yellow = [np.array([30,255,255])]

lower_green = [np.array([31,140,144])]
upper_green = [np.array([52,255,255])]

def get_number_of_objects_in_range(img: cv2.Mat, lower_hsv_limits: list[np.ndarray], upper_hsv_limits: list[np.ndarray]) -> any:
    
    kernel = np.ones((5,5),np.uint8)

    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_img, lower_hsv_limits[0], upper_hsv_limits[0])

    for i in range(len(lower_hsv_limits)):
        temporary_mask = cv2.inRange(hsv_img, lower_hsv_limits[i], upper_hsv_limits[i])
        mask = cv2.bitwise_or(mask, temporary_mask)

    opening_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    dilate_mask = cv2.dilate(opening_mask, kernel , iterations=4)

    contours, _ = cv2.findContours(dilate_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    return len(contours), dilate_mask