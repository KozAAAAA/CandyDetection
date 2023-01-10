import json
from pathlib import Path
from typing import Dict

import click
import cv2
from tqdm import tqdm

import numpy as np
from my_func_and_ranges import *
from my_check import my_check


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
    red_count, red_display = get_number_of_objects_in_range(img, lower_red, upper_red)
    purple_count, purple_display = get_number_of_objects_in_range(img, lower_purple, upper_purple)
    yellow_count, yellow_display = get_number_of_objects_in_range(img, lower_yellow, upper_yellow)
    green_count, green_display = get_number_of_objects_in_range(img, lower_green, upper_green)
    
    # print("red = " + str(red_count))
    # print("purple = " + str(purple_count))
    # print("yellow = " + str(yellow_count))
    # print("green = " + str(green_count))
    
    red = red_count
    yellow = yellow_count
    green = green_count
    purple = purple_count

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
    my_check()


if __name__ == '__main__':
    main()
    
