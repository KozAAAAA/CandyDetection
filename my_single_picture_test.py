import cv2
import numpy as np
from my_func_and_ranges import *


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

img = cv2.imread("data/17.jpg", cv2.IMREAD_COLOR)

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