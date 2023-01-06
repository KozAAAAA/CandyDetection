import json
from pathlib import Path
from typing import Dict

import click
import cv2
from tqdm import tqdm
import glob
import numpy as np


def main():
    img_paths = glob.glob("data/*.jpg")
    
    for img_path in img_paths:
        print(img_path)
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
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

        img_red_masked = cv2.bitwise_and(img, img, mask = red_mask)
        img_purple_masked = cv2.bitwise_and(img, img, mask = purple_mask)
        img_yellow_masked = cv2.bitwise_and(img, img, mask = yellow_mask)
        img_green_masked = cv2.bitwise_and(img, img, mask = green_mask)

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
        
        cv2.imshow("normal", img)
        cv2.imshow("red", img_red_masked)
        cv2.imshow("purple", img_purple_masked)
        cv2.imshow("yellow", img_yellow_masked)
        cv2.imshow("green", img_green_masked)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()