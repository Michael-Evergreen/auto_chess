import cv2
import numpy as np
import math
from ctypes import wintypes, windll
from functools import cmp_to_key
import os

"""
Sets up path and variables for later use
"""
# Creates a kernel
kernel = np.ones((3, 3), np.uint8)

# Folder that stores all characters
folder_path = "G:/all_background_removed_characters/"

# Filters out desktop.ini
all_characters = [character for character in os.listdir(folder_path) if not character.endswith("ini")]

# Count variable for naming later
count = 0

"""
Defines function to sort names with numbers alphabetically then numerically
"""
def winsort(data):
    _StrCmpLogicalW = windll.Shlwapi.StrCmpLogicalW
    _StrCmpLogicalW.argtypes = [wintypes.LPWSTR, wintypes.LPWSTR]
    _StrCmpLogicalW.restype = wintypes.INT

    cmp_fnc = lambda psz1, psz2: _StrCmpLogicalW(psz1, psz2)
    return sorted(data, key=cmp_to_key(cmp_fnc))


"""
Defines main loop that combines images methodically
"""
# Iterates through all 212 characters
for character_index in range(len(all_characters)):

    # Lists all images of the current character, we will call it the main character
    main_character_path = folder_path + all_characters[character_index] + "/"
    main_character_images = winsort([image for image in os.listdir(main_character_path) if image.endswith("png")])

    # Iterates through all images of the main character
    for image_index in range(len(main_character_images)):
        # Necessary processing to get main character's foreground mask and its inverse
        main_image_path = main_character_path + main_character_images[image_index]
        main_image = cv2.imread(main_image_path)
        image_mask = cv2.cvtColor(main_image.copy(), cv2.COLOR_BGR2GRAY)
        _, image_mask = cv2.threshold(image_mask, 5, 255, cv2.THRESH_BINARY)
        image_mask = cv2.dilate(image_mask, kernel, iterations=1)
        image_mask = cv2.erode(image_mask, kernel, iterations=1)
        main_image_foreground = cv2.bitwise_and(main_image, main_image, mask=image_mask)
        main_image_inv_mask = cv2.bitwise_not(image_mask)

        # With each loop, we get 7 other "sub" characters that will stand next to the main
        # we take modulus 212 so we don't goes out of the list
        sub_character_1_path = folder_path + all_characters[(image_index + 1) % 212]
        sub_character_1_images = winsort([image for image in os.listdir(sub_character_1_path) if image.endswith("png")])

        # Each character has 160 images with 20 images for each position. By adding 20 and taking modulus 160 of the sum
        # we make sure that the sub character will stand next to our main
        sub_character_1_image_path = sub_character_1_path + "/" + sub_character_1_images[(image_index + 20) % 160]

        # Similar processing to get foreground mask and its inverse
        sub_image_1 = cv2.imread(sub_character_1_image_path)
        sub_image_1_mask = cv2.cvtColor(sub_image_1.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_1_mask = cv2.threshold(sub_image_1_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_1_mask = cv2.dilate(sub_image_1_mask, kernel, iterations=1)
        sub_image_1_mask = cv2.erode(sub_image_1_mask, kernel, iterations=1)
        sub_image_1_foreground = cv2.bitwise_and(sub_image_1, sub_image_1, mask=sub_image_1_mask)
        sub_image_1_inv_mask = cv2.bitwise_not(sub_image_1_mask)

        # Repeats for all other sub characters
        sub_character_2_path = folder_path + all_characters[(image_index + 2) % 212]
        sub_character_2_images = winsort([image for image in os.listdir(sub_character_2_path) if image.endswith("png")])
        sub_character_2_image_path = sub_character_2_path + "/" + sub_character_2_images[(image_index + 40) % 160]
        sub_image_2 = cv2.imread(sub_character_2_image_path)
        sub_image_2_mask = cv2.cvtColor(sub_image_2.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_2_mask = cv2.threshold(sub_image_2_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_2_mask = cv2.dilate(sub_image_2_mask, kernel, iterations=1)
        sub_image_2_mask = cv2.erode(sub_image_2_mask, kernel, iterations=1)
        sub_image_2_foreground = cv2.bitwise_and(sub_image_2, sub_image_2, mask=sub_image_2_mask)
        sub_image_2_inv_mask = cv2.bitwise_not(sub_image_2_mask)

        sub_character_3_path = folder_path + all_characters[(image_index + 3) % 212]
        sub_character_3_images = winsort([image for image in os.listdir(sub_character_3_path) if image.endswith("png")])
        sub_character_3_image_path = sub_character_3_path + "/" + sub_character_3_images[(image_index + 60) % 160]
        sub_image_3 = cv2.imread(sub_character_3_image_path)
        sub_image_3_mask = cv2.cvtColor(sub_image_3.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_3_mask = cv2.threshold(sub_image_3_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_3_mask = cv2.dilate(sub_image_3_mask, kernel, iterations=1)
        sub_image_3_mask = cv2.erode(sub_image_3_mask, kernel, iterations=1)
        sub_image_3_foreground = cv2.bitwise_and(sub_image_3, sub_image_3, mask=sub_image_3_mask)
        sub_image_3_inv_mask = cv2.bitwise_not(sub_image_3_mask)

        sub_character_4_path = folder_path + all_characters[(image_index + 4) % 212]
        sub_character_4_images = winsort([image for image in os.listdir(sub_character_4_path) if image.endswith("png")])
        sub_character_4_image_path = sub_character_4_path + "/" + sub_character_4_images[(image_index + 80) % 160]
        sub_image_4 = cv2.imread(sub_character_4_image_path)
        sub_image_4_mask = cv2.cvtColor(sub_image_4.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_4_mask = cv2.threshold(sub_image_4_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_4_mask = cv2.dilate(sub_image_4_mask, kernel, iterations=1)
        sub_image_4_mask = cv2.erode(sub_image_4_mask, kernel, iterations=1)
        sub_image_4_foreground = cv2.bitwise_and(sub_image_4, sub_image_4, mask=sub_image_4_mask)
        sub_image_4_inv_mask = cv2.bitwise_not(sub_image_4_mask)

        sub_character_5_path = folder_path + all_characters[(image_index + 5) % 212]
        sub_character_5_images = winsort([image for image in os.listdir(sub_character_5_path) if image.endswith("png")])
        sub_character_5_image_path = sub_character_5_path + "/" + sub_character_5_images[(image_index + 100) % 160]
        sub_image_5 = cv2.imread(sub_character_5_image_path)
        sub_image_5_mask = cv2.cvtColor(sub_image_5.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_5_mask = cv2.threshold(sub_image_5_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_5_mask = cv2.dilate(sub_image_5_mask, kernel, iterations=1)
        sub_image_5_mask = cv2.erode(sub_image_5_mask, kernel, iterations=1)
        sub_image_5_foreground = cv2.bitwise_and(sub_image_5, sub_image_5, mask=sub_image_5_mask)
        sub_image_5_inv_mask = cv2.bitwise_not(sub_image_5_mask)

        sub_character_6_path = folder_path + all_characters[(image_index + 6) % 212]
        sub_character_6_images = winsort([image for image in os.listdir(sub_character_6_path) if image.endswith("png")])
        sub_character_6_image_path = sub_character_6_path + "/" + sub_character_6_images[(image_index + 120) % 160]
        sub_image_6 = cv2.imread(sub_character_6_image_path)
        sub_image_6_mask = cv2.cvtColor(sub_image_6.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_6_mask = cv2.threshold(sub_image_6_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_6_mask = cv2.dilate(sub_image_6_mask, kernel, iterations=1)
        sub_image_6_mask = cv2.erode(sub_image_6_mask, kernel, iterations=1)
        sub_image_6_foreground = cv2.bitwise_and(sub_image_6, sub_image_6, mask=sub_image_6_mask)
        sub_image_6_inv_mask = cv2.bitwise_not(sub_image_6_mask)

        sub_character_7_path = folder_path + all_characters[(image_index + 7) % 212]
        sub_character_7_images = winsort([image for image in os.listdir(sub_character_7_path) if image.endswith("png")])
        sub_character_7_image_path = sub_character_7_path + "/" + sub_character_7_images[(image_index + 140) % 160]
        sub_image_7 = cv2.imread(sub_character_7_image_path)
        sub_image_7_mask = cv2.cvtColor(sub_image_7.copy(), cv2.COLOR_BGR2GRAY)
        _, sub_image_7_mask = cv2.threshold(sub_image_7_mask, 5, 255, cv2.THRESH_BINARY)
        sub_image_7_mask = cv2.dilate(sub_image_7_mask, kernel, iterations=1)
        sub_image_7_mask = cv2.erode(sub_image_7_mask, kernel, iterations=1)
        sub_image_7_foreground = cv2.bitwise_and(sub_image_7, sub_image_7, mask=sub_image_7_mask)
        sub_image_7_inv_mask = cv2.bitwise_not(sub_image_7_mask)

        # Gets 1 of the 20 background images each loop
        background = cv2.imread("G:/background/" + str(image_index % 20) + ".png")

        # Blacks out the parts where our characters stand
        background = cv2.bitwise_and(background, background, mask=main_image_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_1_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_2_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_3_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_4_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_5_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_6_inv_mask)
        background = cv2.bitwise_and(background, background, mask=sub_image_7_inv_mask)

        # Combines all images together
        result = cv2.add(background, sub_image_7_foreground)
        result = cv2.add(result, sub_image_6_foreground)
        result = cv2.add(result, sub_image_5_foreground)
        result = cv2.add(result, sub_image_4_foreground)
        result = cv2.add(result, sub_image_3_foreground)
        result = cv2.add(result, sub_image_2_foreground)
        result = cv2.add(result, sub_image_1_foreground)
        result = cv2.add(result, main_image_foreground)

        # Writes to a folder
        cv2.imwrite("G:/result/" + str(count) + ".png", result)

        # Gets the paths of the labels
        main_txt_path = main_image_path[:-4] + ".txt"
        sub_txt_1_path = sub_character_1_image_path[:-4] + ".txt"
        sub_txt_2_path = sub_character_2_image_path[:-4] + ".txt"
        sub_txt_3_path = sub_character_3_image_path[:-4] + ".txt"
        sub_txt_4_path = sub_character_4_image_path[:-4] + ".txt"
        sub_txt_5_path = sub_character_5_image_path[:-4] + ".txt"
        sub_txt_6_path = sub_character_6_image_path[:-4] + ".txt"
        sub_txt_7_path = sub_character_7_image_path[:-4] + ".txt"

        # Reads all the labels and combines them
        with open("G:/result/" + str(count) + ".txt", "w+") as f:
            f.write(open(main_txt_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_1_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_2_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_3_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_4_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_5_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_6_path, "r").read().strip() + "\n")
            f.write(open(sub_txt_7_path, "r").read().strip() + "\n")

        count += 1
