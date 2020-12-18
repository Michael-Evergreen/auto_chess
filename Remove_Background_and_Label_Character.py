from ctypes import wintypes, windll
from functools import cmp_to_key
import cv2
import os
import shutil
from lxml import etree
from PIL import Image
import csv
import numpy as np


"""
Loads constants to ram
"""

# Images shape
IMAGE_WIDTH = 848
IMAGE_HEIGHT = 212


# 8 positions where characters stand, we will blacken all other parts of the images to remove noises
POS_LIST = [(105, 140), (105, 202), (105, 294), (105, 388), (105, 480), (105, 542), (105, 634), (105, 726)]


# Mapping characters names to their numbers
f = open('heroes_names.txt', "r").read().splitlines()
dict = {}
count = 0
for hero in f:
    dict[hero] = count
    count += 1


"""
Defines remove-background function. Some parameters have default values and can be used for most cases. However,  
there are abnormalities that require tweaking (characters that are too big, characters whose colors are similar to the
background's they stand on)
"""
def remove_background(background_image_path, character_image_path, hero_height=170, hero_width=150, threshold=1200):
    # Reads images
    background_image = cv2.imread(background_image_path)
    character_image = cv2.imread(character_image_path)

    # Creates a model
    backgroundSubtractor = cv2.createBackgroundSubtractorKNN(history=1, dist2Threshold=threshold)

    # Gaussian blurs images to "harmonize" them
    background_image = cv2.GaussianBlur(background_image, (5, 5), 0)
    character_image = cv2.GaussianBlur(character_image, (5, 5), 0)

    # Lets the model "learn" the background, it needs at least 4 frames
    backgroundSubtractor.apply(background_image, learningRate=0.99)
    backgroundSubtractor.apply(background_image, learningRate=0.99)
    backgroundSubtractor.apply(background_image, learningRate=0.99)
    backgroundSubtractor.apply(background_image, learningRate=0.99)

    # Model identifies the differences, i.e., the character, from background and return a mask
    foregroundmask = backgroundSubtractor.apply(character_image, learningRate=0)

    # Creates a kernel
    kernel = np.ones((3, 3), np.uint8)

    # Applies various denoising methods to the mask
    foregroundmask = cv2.morphologyEx(foregroundmask, cv2.MORPH_OPEN, kernel)
    foregroundmask = cv2.morphologyEx(foregroundmask, cv2.MORPH_CLOSE, kernel)
    foregroundmask = cv2.fastNlMeansDenoising(foregroundmask, None, 30, 7, 21)

    # Removes dispersed, low-value noises and cranks up character's pixels' values
    ret, foregroundmask = cv2.threshold(foregroundmask, 50, 255, cv2.THRESH_BINARY)

    # Gets character's position coordinate
    position = int(character_image_path[-8])
    position_coordinate = POS_LIST[position-1]

    # Calculates a rectangle where character stands and the rest of the image will be set to 0
    # In case character is too big then the rectangle's height is set to be the same as the image's height
    if position_coordinate[0] > hero_height / 2:
        to_be_removed_ara_height_1 = int(position_coordinate[0] - hero_height / 2)
    else:
        to_be_removed_ara_height_1 = 0

    if (position_coordinate[0] + hero_height / 2) < IMAGE_HEIGHT:
        to_be_removed_ara_height_2 = int(position_coordinate[0] + hero_height / 2)
    else:
        to_be_removed_ara_height_2 = IMAGE_HEIGHT

    if position_coordinate[1] > hero_width / 2:
        to_be_removed_ara_width_1 = int(position_coordinate[1] - hero_width / 2)
    else:
        to_be_removed_ara_width_1 = 0

    if (position_coordinate[1] + hero_width / 2) < IMAGE_WIDTH:
        to_be_removed_ara_width_2 = int(position_coordinate[1] + hero_width / 2)
    else:
        to_be_removed_ara_width_2 = IMAGE_WIDTH

    # Sets irrelevant parts of the image to 0
    foregroundmask[0: to_be_removed_ara_height_1, 0:IMAGE_WIDTH] = 0
    foregroundmask[to_be_removed_ara_height_2: IMAGE_HEIGHT, 0:IMAGE_WIDTH] = 0
    foregroundmask[0: IMAGE_HEIGHT, 0: to_be_removed_ara_width_1] = 0
    foregroundmask[0: IMAGE_HEIGHT, to_be_removed_ara_width_2: IMAGE_WIDTH] = 0

    # Applies bitwise_and to the original image.
    background_removed_image = cv2.bitwise_and(character_image, character_image, mask=foregroundmask)

    # Returns mask and background-removed image
    return foregroundmask, background_removed_image


"""
Defines function to get the biggest contour from mask
"""
def get_image_contour_box(foregroundmask):
    # Retrieves contours
    contours, hierarchy = cv2.findContours(foregroundmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Gets a list of contours' sizes
    areas = [cv2.contourArea(c) for c in contours]

    # Sorts and gets the index the biggest contour, also, gets the bounding rectangle of it.
    temp_areas = areas
    temp_areas = sorted(temp_areas, reverse=True)
    x, y, w, h = cv2.boundingRect(contours[areas.index(temp_areas[0])])

    # Return coordinate, width, height of bounding box
    return x, y, w, h


"""
Defines function to create a txt file that stores character's number and bounding box
"""
def create_label_and_draw_bounding_box(character_image_path, character_number, x, y, w, h):
    # Changes coordinate, width, height to YOLO format
    x_yolo = (x + w) / 2 / IMAGE_WIDTH
    y_yolo = (y + h) / 2 / IMAGE_HEIGHT
    width_yolo = w / IMAGE_WIDTH
    height_yolo = h / IMAGE_HEIGHT

    # Writes txt file
    with open(character_image_path[0:-4] + ".txt", "w+") as f:
        f.write(f"{character_number} {x_yolo} {y_yolo} {width_yolo} {height_yolo}")


"""
Defines main
"""
def main():
    # Defines paths
    all_characters_path = 'G:/all_characters/'
    all_background_path = 'G:/background/'
    all_background_removed_characters_path = 'G:/all_background_removed_characters/'

    # Lists all characters' folders
    all_characters = os.listdir(all_characters_path)

    # Iterates through all folder
    for character in all_characters:

        # Lists all images from each folder
        character_path = all_characters_path + character + "/"
        all_images = [image for image in os.listdir(character_path) if image.endswith("jpg")]

        # Iterates through all images
        for image in all_images:
            image_path = character_path + image
            background_path = all_background_path + "background_pos_" + image[-8] + ".png"

            # Removes background from image
            foregroundmask, background_removed_image = remove_background(background_path, image_path)

            # Gets the biggest contour from image
            x, y, w, h = get_image_contour_box(foregroundmask)

            # Gets character's number
            character_number = dict[character]

            # Goes to character folder
            os.chdir(character_path)

            # Creates label for image
            create_label_and_draw_bounding_box(image_path, character_number, x, y, w, h)

            # Goes to background-removed character folder
            background_removed_character_path = all_background_removed_characters_path + character
            os.chdir(background_removed_character_path)

            # Saves background-removed images and creates label
            cv2.imwrite(background_removed_character_path + image, foregroundmask)
            create_label_and_draw_bounding_box(background_removed_character_path + image, character_number, x, y, w, h)


if __name__ == "__main__":
        main()