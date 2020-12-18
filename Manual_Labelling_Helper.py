import numpy as np
import cv2
import pyautogui
import keyboard
import tkinter as tk
import time
import os

"""
Defines global variables
"""

# Image relevant information to draw boxes
image_number = 0
list_of_boxes = []
background_number = 1
threshold = 1200
box_number = 0

# The distance from the top-left corner of our screen (1920x1080) to the image on labelImg
labelImg_distance_x = 109
labelImg_distance_y = 435

"""
Defines function to get image biggest objects' bounding boxes
"""
def get_image_bounding_boxes(image_number, background_number, threshold):
    # Loads image
    image_path = 'G:/ingame_images/' + str(image_number) + ".jpg"
    ori_image = cv2.imread(image_path)

    # Creates a model
    backgroundSubtractor = cv2.createBackgroundSubtractorKNN(history=50, dist2Threshold=threshold)

    # Lets model learns the new background
    background_path = 'G:/ingame_background/' + str(background_number) + ".jpg"
    background = cv2.imread(background_path)
    background= cv2.GaussianBlur(background, (5, 5), 0)
    backgroundSubtractor.apply(background, learningRate=0.99)
    backgroundSubtractor.apply(background, learningRate=0.99)
    backgroundSubtractor.apply(background, learningRate=0.99)
    backgroundSubtractor.apply(background, learningRate=0.99)

    # Model identifies the differences, i.e., the characters, from background and return a mask
    blured = cv2.GaussianBlur(ori_image, (5, 5), 0)
    foregroundmask = backgroundSubtractor.apply(blured, learningRate=0)

    # Creates a kernel
    kernel = np.ones((3, 3), np.uint8)

    # Applies various denoising methods to the mask
    foregroundmask = cv2.morphologyEx(foregroundmask, cv2.MORPH_OPEN, kernel)
    foregroundmask = cv2.morphologyEx(foregroundmask, cv2.MORPH_CLOSE, kernel)
    foregroundmask = cv2.fastNlMeansDenoising(foregroundmask, None, 30, 7, 21)

    # Removes dispersed, low-value noises and cranks up character's pixels' values
    ret, foregroundmask = cv2.threshold(foregroundmask, 50, 255, cv2.THRESH_BINARY)

    # Retrieves contours
    contours, hierarchy = cv2.findContours(foregroundmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Gets a list of contours' sizes
    areas = [cv2.contourArea(c) for c in contours]

    # Sorts for the biggest contours
    temp_areas = areas
    temp_areas = sorted(temp_areas, reverse=True)

    # gets a list of indexes of 10 biggest contours
    list_of_indexs = []
    for i in range(0, 10):
        list_of_indexs.append(areas.index(temp_areas[i]))

    # returns the on-screen coordinates of those contours
    list_of_boxes = []
    for i in range (0, 10):
        x, y, w, h = cv2.boundingRect(contours[list_of_indexs[i]])
        list_of_boxes.append(((x+labelImg_distance_x, y+labelImg_distance_y), ((x+w+labelImg_distance_x), (y+h+labelImg_distance_y))))
    return(list_of_boxes)


"""
Defines main with a tkinter main event loop for input
"""
def main():
    global image_number
    global list_of_boxes
    global box_number
    while True:
        # Creates a simple GUI when ctrl+x are pressed to enter values
        if keyboard.is_pressed('ctrl+x'):
            root = tk.Tk()
            canvas1 = tk.Canvas(root, width=400, height=300)
            canvas1.pack()

            # Creates 3 entries for necessary information to find bounding boxes
            image_entry = tk.Entry(root)
            background_entry = tk.Entry(root)
            threshold_entry = tk.Entry(root)
            canvas1.create_window(220, 20, window=image_entry)
            canvas1.create_window(220, 100, window=background_entry)
            canvas1.create_window(220, 190, window=threshold_entry)

            # Help text
            helptext = tk.Label(root, text=("Press alt+d to go to next image\n      Press alt+a to go to previous image"))
            canvas1.create_window(90, 60, window=helptext)

            # Defines function to update image's number and path when button is clicked
            def inputimagenumber():
                global image_number
                image_number = int(image_entry.get())

                # Gets a list of all boxes coordinates
                global list_of_boxes
                list_of_boxes = get_image_bounding_boxes(image_number, background_number, threshold)

                label1 = tk.Label(root, text=("Current image: " + str(image_number)))
                canvas1.create_window(310, 20, window=label1)

                # Starts counting from the first box again
                global box_number
                box_number = 0

            # Function to update background's number
            def inputbackground():
                global background_number
                background_number = background_entry.get()
                label2 = tk.Label(root, text=("Current background: " + str(background_number)))
                canvas1.create_window(310, 100, window=label2)


            # Function to update threshold
            def inputthreshold():
                global threshold
                threshold = int(threshold_entry.get())
                label3 = tk.Label(root, text=("Current threshold: " + str(threshold)))
                canvas1.create_window(310, 190, window=label3)

            # Draws buttons
            image_button = tk.Button(text='Input Image Number', command=inputimagenumber)
            canvas1.create_window(80, 20, window=image_button)

            background_button = tk.Button(text='Input Background Number', command=inputbackground)
            canvas1.create_window(78, 100, window=background_button)

            threshold_button = tk.Button(text='Input Threshold', command=inputthreshold)
            canvas1.create_window(80, 190, window=threshold_button)

            root.mainloop()

        # Goes to next image when alt+d are pressed
        if keyboard.is_pressed('alt+d'):
            image_number += 1
            list_of_boxes = get_image_bounding_boxes(image_number, background_number, threshold)
            print("Acquired boxes for image " + str(image_number))
            box_number = 0
            time.sleep(1)

        # Goes to next image when alt+a are pressed
        if keyboard.is_pressed('alt+a'):
            image_number -= 1
            list_of_boxes = get_image_bounding_boxes(image_number, background_number, threshold)
            print("Acquired boxes for image " + str(image_number))
            box_number = 0
            time.sleep(1)

        # Draw boxes from largest to smallest each time tab is pressed
        if keyboard.is_pressed("tab"):
            pyautogui.dragTo(list_of_boxes[box_number][1])
            print("Drawing box number " + str(box_number))
            box_number +=1
            time.sleep(1)


if __name__ == "__main__":
        main()
