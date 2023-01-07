import json
from pathlib import Path
from typing import Dict

import click
import cv2
from tqdm import tqdm

import numpy as np


def detect(img_path: str) -> Dict[str, int]:
    """Object detection function, according to the project description, to implement.

    Parameters
    ----------
    img_path : str
        Path to processed image.

    Returns
    -------
    Dict[str, int]
        Dictionary with quantity of each object.
    """
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    #TODO: Implement detection method.

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

    red_mask = cv2.dilate(red_mask, kernel , iterations=3)
    purple_mask = cv2.dilate(purple_mask, kernel , iterations=3)
    yellow_mask = cv2.dilate(yellow_mask, kernel , iterations=3)
    green_mask = cv2.dilate(green_mask, kernel , iterations=3)

    red_opening = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    purple_opening = cv2.morphologyEx(purple_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    yellow_opening = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    green_opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=2)

    red_contours, _ = cv2.findContours(red_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    purple_contours, _ = cv2.findContours(purple_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    yellow_contours, _ = cv2.findContours(yellow_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    green_contours, _ = cv2.findContours(green_opening,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print("red = " + str(len(red_contours)))
    print("purple = " + str(len(purple_contours)))
    print("yellow = " + str(len(yellow_contours)))
    print("green = " + str(len(green_contours)))
    
    red = len(red_contours)
    yellow = len(yellow_contours)
    green = len(green_contours)
    purple = len(purple_contours)

    return {'red': red, 'yellow': yellow, 'green': green, 'purple': purple}


@click.command()
@click.option('-p', '--data_path', help='Path to data directory', type=click.Path(exists=True, file_okay=False, path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path), required=True)
def main(data_path: Path, output_file_path: Path):
    img_list = data_path.glob('*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        fruits = detect(str(img_path))
        results[img_path.name] = fruits

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)


if __name__ == '__main__':
    main()
