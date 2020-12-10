# players coord
# a = (1602, 233)
# b = (1602, 320)
# c = (1602, 409)
# d = (1602, 497)
# e = (1602, 586)
# f = (1602, 670)
# g = (1602, 758)
# h = (1602, 844)

# constant = (312, 978)


import os
# os.chdir("G:/darknet/")
# bashCommand = "G:\darknet/darknet.exe detect thresh_cfg.cfg G:\darknetsave/yolov4-obj_last_25.weights G:\old_butgood_obj/101.jpg"
# os.system(bashCommand)
import shutil

import cv2
# import time
def show(img):
    cv2.imshow("aaa",img)
    cv2.waitKey(0)
# CONFIDENCE_THRESHOLD = 0.3
# NMS_THRESHOLD = 0.1
# COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
#
# class_names = []
# with open("classes.txt", "r") as f:
#     class_names = [cname.strip() for cname in f.readlines()]
#
# vc = cv2.VideoCapture("G:\old_butgood_obj/101.jpg")
#
# net = cv2.dnn.readNet("G:\darknetsave/yolov4-obj_last_25.weights", "G:\darknet/thresh_cfg.cfg")
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
#
# model = cv2.dnn_DetectionModel(net)
# model.setInputParams(size=(448, 448), scale=1 / 255)
#
# while cv2.waitKey(0) < 1:
#     (grabbed, frame) = vc.read()
#     if not grabbed:
#         exit()
#
#     start = time.time()
#     classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
#     end = time.time()
#
#     start_drawing = time.time()
#     for (classid, score, box) in zip(classes, scores, boxes):
#         color = COLORS[int(classid) % len(COLORS)]
#         label = "%s : %f" % (class_names[classid[0]], score)
#         cv2.rectangle(frame, box, color, 1)
#         cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 2)
#     end_drawing = time.time()
#
#     fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (
#     1 / (end - start), (end_drawing - start_drawing) * 1000)
#     cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#     cv2.imshow("detections", frame)


import cv2
import time

# CONFIDENCE_THRESHOLD = 0.1
# NMS_THRESHOLD = 0.0000000000000000000001
# COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255), (0, 0, 255)]
#
# class_names = []
# with open("classes.txt", "r") as f:
#     class_names = [cname.strip() for cname in f.readlines()]
#
# vc = cv2.imread("G:\old_butgood_obj/101.jpg")
# vc = cv2.cvtColor(vc, cv2.COLOR_BGR2RGB)
#
# net = cv2.dnn.readNet("G:\darknetsave/yolov4-obj_last_25.weights", "G:\darknet/thresh_cfg.cfg")
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
#
# model = cv2.dnn_DetectionModel(net)
# model.setInputParams(size=(448, 448), scale=1 / 255)
#
#
#
# classes, scores, boxes = model.detect(vc, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
#
# boxa = [500, 22, 22, 22]
# for (classid, score, box) in zip(classes, scores, boxes):
#     color = COLORS[int(classid) % len(COLORS)]
#     label = "%s : %f" % (class_names[classid[0]], score)
#     cv2.rectangle(vc, box, color, 1)
#     cv2.rectangle(vc, boxa, color, 1)
#     cv2.putText(vc, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 2)
#
# cv2.imshow("detections", vc)
#
# # cv2.waitKey(0)
# for (classid, score, box) in zip(classes, scores, boxes):
#     print(class_names[classid[0]], ": ", score, ": ", type(box), classid)
#
# # print(cv2.__version__)
#
# # cv2.imshow("s", vc)
# cv2.waitKey(0)
import cv2
import json
import os
import numpy as np
import shutil
from matplotlib import pyplot as plt

# HEIGHT = 212
# WIDTH = 848
# COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255), (0, 0, 255), (255, 255, 255), (125, 0, 255), (255, 0, 125), (125, 255, 0), (0, 255, 125), (0, 125, 255), (255, 125, 0), (125, 75, 0), (0, 75, 125), (0, 125, 75), (75, 125, 0), (75, 0, 125), (125, 0, 75)]
# f = open("G:/darknet/result.json")
# data = json.load(f)
#
player1, player2, player3, player4, player5, player6, player7, player8 = ([] for i in range(8))
list_of_players = [player1, player2, player3, player4, player5, player6, player7, player8]
#
# first_half = np.zeros((0,848,3), dtype=np.uint8)
# second_half = np.zeros((0,0,3), dtype=np.uint8)
#
# for i in range(1, len(data)+1):
#     img = cv2.imread(f"C:/autochess_data/{i}.jpg")
#     for hero in data[i-1]['objects']:
#         list_of_players[i].append(hero['name'])
#         x_start = round(hero["relative_coordinates"]["center_x"]*WIDTH - hero["relative_coordinates"]["width"]*WIDTH/2)
#         x_end = round(hero["relative_coordinates"]["center_x"]*WIDTH + hero["relative_coordinates"]["width"]*WIDTH/2)
#         y_start = round(hero["relative_coordinates"]["center_y"]*HEIGHT - hero["relative_coordinates"]["height"]*HEIGHT/2)
#         y_end = round(hero["relative_coordinates"]["center_y"]*HEIGHT + hero["relative_coordinates"]["height"]*HEIGHT/2)
#         cv2.rectangle(img, (x_start, y_start), (x_end, y_end), COLORS[int(hero['class_id']) % len(COLORS)], 1)
#         cv2.putText(img, hero['name'], (x_start, y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[int(hero['class_id']) % len(COLORS)], 1)
#         cv2.putText(img, f"player{i}",(0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
#     os.chdir("C:/autochess_data")
#
#     first_half = cv2.vconcat([first_half, img])
# cv2.imwrite("all_predictions.jpg", first_half)
#


# img_rgb = cv2.imread("G:/asdff.png")
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread("G:/morph.png",0)
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# os.chdir("G:/")
# cv2.imwrite('res.png',img_rgb)

# fill_color = [0, 255, 0] # any BGR color value to fill with
# mask_value = 255            # 1 channel white (can be any non-zero uint8 value)
#
# ori = cv2.imread("G:/AA.jpg")
# w, h = ori.shape[:-1]
#
# inverted = cv2.bitwise_not(ori)
# grayed = cv2.cvtColor(inverted, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(grayed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# # cv2.drawContours(grayed, contours, -1, (0,255,0),3)
#
# stencil = np.zeros(ori.shape[:-1]).astype(np.uint8)
# cv2.fillPoly(stencil, contours, mask_value)
#
# sel = stencil != mask_value # select everything that is not mask_value
# ori[sel] = fill_color            # and fill it with fill_color
#
# cv2.imshow("asd", ori)
# cv2.waitKey(0)
# os.chdir("G:/")
# cv2.imwrite("resulta.jpg", img)

# print(cv2.imread("G:/icon/AA.jpg").shape)
# for file in os.listdir("G:LilyGreen/icon/"):
#     file_path = "G:LilyGreen/icon/" + file
#     ori = cv2.imread(file_path)
#     w, h = ori.shape[:-1]
#     mask = np.zeros([w + 2, h + 2], np.uint8)
#     result = ori.copy()
#     cv2.floodFill(result, mask, (0,0), (48,48,48), (1,0,0), (1,0,0), flags=8)
#     # cv2.floodFill(result, mask, (1,30), (48,48,48), (1,1,1), (1,1,1), flags=8)
#     # cv2.floodFill(result, mask, (31,0), (48,48,48), (1,1,1), (1,1,1), flags=8)
#     # cv2.floodFill(result, mask, (31,31), (48,48,48), (1,1,1), (1,1,1), flags=8)
#     os.chdir("G:LilyGreen/newicon/")
#     cv2.imwrite(file, result)
# import pyautogui
# import time
# pyautogui.displayMousePosition()
# import keyboard
# time.sleep(2)
# count = 0
# while count != 120:
#     c = count
#     keyboard.press_and_release('ctrl + o')
#     a = 375,462
#     time.sleep(0.3)
#     pyautogui.moveTo(a)
#     pyautogui.click()
#     while c > 0:
#         keyboard.press_and_release('right')
#         c -= 1
#
#     keyboard.press_and_release('enter')
#
#     b = 976,1037
#     pyautogui.moveTo(b)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     c = 695, 113
#     pyautogui.moveTo(c)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     d = 240, 76
#     pyautogui.moveTo(d)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     e = 8, 154
#
#     f = 260, 155
#
#     g = 258, 405
#
#     j = 9, 405
#
#     pyautogui.moveTo(e)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     pyautogui.moveTo(f)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     pyautogui.moveTo(g)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     pyautogui.moveTo(j)
#     pyautogui.click()
#     time.sleep(0.2)
#
#     count += 1
#     keyboard.press_and_release("ctrl + s")
#

# axe = np.zeros((0, 0, 3), dtype=np.uint8)
# for file in os.listdir("G:/icon"):
#     file_path = "G:/icon/" + file
#     axe = cv2.imread(file_path, 0)
# axe = cv2.imread("G:/combined.png", 0)


# cv2.imshow('asd', axe)
# cv2.waitKey(0)

# img_rgb = cv2.imread("G:/Video/Bloodseeker.png")
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#
# template = cv2.imread("G:/Blood.png", 0)
#
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.7
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
# os.chdir("G:/")
# # cv2.imshow("template", template)
# cv2.imshow("img", img_gray)
# cv2.waitKey(0)

# for file in os.listdir("G:/temp/"):
#     file_path = "G:/temp/" + file
#     new_file_path = file_path[0:-21] + ".png"
#     shutil.move(file_path, new_file_path)

# for file in os.listdir("G:/temp"):
#     file_path = "G:/temp/" + file
#     overlay = cv2.imread(file_path, -1)
#     # overlay = cv2.GaussianBlur(overlay, (3, 3), 0)
#     background = cv2.imread("G:/bg.png", -1)
#     h, w, c = overlay.shape
#     # print(overlay.shape[:-1])
#     mask = background[4:h +4, 0:w]
#
#     alpha = overlay[:, :, 3] / 255.0
#     mask[:, :, 0] = (1. - alpha) * mask[:, :, 0] + alpha * overlay[:, :, 0]
#     mask[:, :, 1] = (1. - alpha) * mask[:, :, 1] + alpha * overlay[:, :, 1]
#     mask[:, :, 2] = (1. - alpha) * mask[:, :, 2] + alpha * overlay[:, :, 2]
#
#     background[4:h +4, 0:w] = mask
#     # cv2.imshow('comasdpng', mask)
#     # cv2.imshow('combined.png', background)
#     # cv2.waitKey(0)
#     pngname = file[0: -4] + ".png"
#     background = cv2.GaussianBlur(background, (3, 3), 0)
#     os.chdir("G:/Video")
#     cv2.imwrite(pngname, background)


# overlay = cv2.imread("G:/Video/Axe.png", -1)
# cv2.imshow("img", overlay)
# cv2.waitKey(0)
# background = cv2.imread("G:/bg.png", -1)

# import requests
# from bs4 import BeautifulSoup
# import os
#
# url = 'https://dota2.gamepedia.com/Category:Hero_minimap_icons'
#
# def imagedown(url, folder):
#     try:
#         os.mkdir(os.path.join(os.getcwd(), folder))
#     except:
#         pass
#     os.chdir(os.path.join(os.getcwd(), folder))
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     images = soup.find_all('img')
#     for image in images:
#         name = image['alt']
#         link = image['src']
#         with open(name.replace(' ', '-').replace('/', '') + '.png', 'wb') as f:
#             im = requests.get(link)
#             f.write(im.content)
#             print('Writing: ', name)
#imagedown(url, 'whatever')

# img_rgb = cv2.imread("G:/Video/Bloodseeker.png")
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#
# template = cv2.imread("G:/Blood.png", 0)
#
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.7
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
# os.chdir("G:/")
# # cv2.imshow("template", template)
# cv2.imshow("img", img_gray)
# cv2.waitKey(0)

# namelist = [
#     'AA',
#     'Abaddon',
#     'Alchemist',
#     'AM',
#     'Arc',
#     'Axe',
#     'Bane',
#     'Barathum',
#     'Batrider',
#     'BB',
#     'BeastMaster',
#     'BH',
#     'Blood',
#     'Brood',
#     'Centaur',
#     'Chaos',
#     'Chen',
#     'Clinkz',
#     'Clock',
#     'CM',
#     'DarkWillow',
#     'Dazzle',
#     'Disruptor',
#     'Doom',
#     'DP',
#     'DragonKnight',
#     'Drow',
#     'DS',
#     'EarthShaker',
#     'EarthSpirit',
#     'Elder',
#     'EmberSpirit',
#     'Enchantress',
#     'Enigma',
#     'Grandma',
#     'Grim',
#     'Gyro',
#     'Huskar',
#     'IceDuck',
#     'Invoker',
#     'IO',
#     'Jakiro',
#     'Juggernaut',
#     'KOTL',
#     'Kunkka',
#     'LC',
#     'LD',
#     'Leshrac',
#     'Lich',
#     'Lina',
#     'Lion',
#     'Luna',
#     'Lycan',
#     'Magnus',
#     'Mars',
#     'Medusa',
#     'Meepo',
#     'Mirana',
#     'MonkeyKing',
#     'Morph',
#     'Naga',
#     'Naix',
#     'Necrophos',
#     'Nevermore',
#     'NP',
#     'NS',
#     'Nyx',
#     'OD',
#     'OgreMagi',
#     'OmniKnight',
#     'Oracle',
#     'Panda',
#     'Pangolier',
#     'Phoenix',
#     'PhuongAnh',
#     'PhuongLinh',
#     'Puck',
#     'Pudge',
#     'Pugna',
#     'QOP',
#     'Razor',
#     'Riki',
#     'Rubik',
#     'SandKing',
#     'SD',
#     'ShadowShaman',
#     'Silencer',
#     'SkeletonKing',
#     'SkywrathMage',
#     'Sladar',
#     'Slark',
#     'Sniper',
#     'Spectre',
#     'Storm',
#     'Sven',
#     'TB',
#     'Terrorist',
#     'Tide',
#     'Timber',
#     'Tinker',
#     'Tiny',
#     'TramAnh',
#     'Treant',
#     'Troll',
#     'Tuskar',
#     'Underlord',
#     'Undying',
#     'Ursa',
#     'Venom',
#     'Viper',
#     'Visage',
#     'Void',
#     'VoidSpirit',
#     'VS',
#     'Warlock',
#     'Weaver',
#     'WindRanger',
#     'WitchDoctor',
#     'WraithKing',
#     'Zeus'
# ]
#
# # loads all hero icons to memory
# count = 0
# hero_icon_dict = {}
# for file in os.listdir('G:/icon'):
#     file_path = "G:/icon/" + file
#     hero_icon_dict[namelist[count]] = cv2.imread(file_path)
#     count +=1
#
# # loads level icons to memory
# level_dict = {}
# level_dict[""] = cv2.imread("G:/level/1.png", 0)
# level_dict["2"] = cv2.imread("G:/level/2.png", 0)
# level_dict["3"] = cv2.imread("G:/level/3.png", 0)

# count2 = 0
# while count2 <120:
#     res = cv2.matchTemplate(dict[namelist[count2]],template,cv2.TM_CCOEFF_NORMED)
#     threshold = 0.7
#     loc = np.where(res >= threshold)
#     if loc[0].size > 0:
#         print(namelist[count2])
#         break
#     count2 +=1
import pyautogui
import keyboard
import time
# while True:
#     if keyboard.is_pressed("q"):
#         posXY = pyautogui.position()
#         print(pyautogui.position(), pyautogui.pixel(posXY[0], posXY[1]))
#         time.sleep(0.3)
#     if keyboard.is_pressed("m"):
#         break

"""
33 x 35 pixels each
711-743 744-766
221-256

"""




#
# ori = cv2.imread("G:/asdff.png")
# plt_image = cv2.cvtColor(ori, cv2.COLOR_BGR2RGB)
# imgplot = plt.imshow(plt_image)
#
# HERO_ICON_WIDTH = 33
# FIRST_X_START = 711
# FIRST_X_END = 744
#
# SECOND_X_START = FIRST_X_START + HERO_ICON_WIDTH
# SECOND_X_END = FIRST_X_END + HERO_ICON_WIDTH
#
# THIRD_X_START = SECOND_X_START + HERO_ICON_WIDTH + 1
# THIRD_X_END = SECOND_X_END + HERO_ICON_WIDTH + 1
#
# FOURTH_X_START = THIRD_X_START + HERO_ICON_WIDTH
# FOURTH_X_END = THIRD_X_END + HERO_ICON_WIDTH
#
# FIFTH_X_START = FOURTH_X_START + HERO_ICON_WIDTH
# FIFTH_X_END = FOURTH_X_END + HERO_ICON_WIDTH
#
# SIXTH_X_START = FIFTH_X_START + HERO_ICON_WIDTH + 1
# SIXTH_X_END = FIFTH_X_END + HERO_ICON_WIDTH + 1
#
# SEVENTH_X_START = SIXTH_X_START + HERO_ICON_WIDTH
# SEVENTH_X_END = SIXTH_X_END + HERO_ICON_WIDTH
#
# EIGHTH_X_START = SEVENTH_X_START + HERO_ICON_WIDTH
# EIGHTH_X_END = SEVENTH_X_END + HERO_ICON_WIDTH
#
# NINTH_X_START = EIGHTH_X_START + HERO_ICON_WIDTH + 1
# NINTH_X_END = EIGHTH_X_END + HERO_ICON_WIDTH + 1
#
# TENTH_X_START = NINTH_X_START + HERO_ICON_WIDTH
# TENTH_X_END = NINTH_X_END + HERO_ICON_WIDTH
#
#
# PLAYER_DISTANCE = 88
# FIRST_Y_START = 221
# FIRST_Y_END = 256
#
# SECOND_Y_START = FIRST_Y_START + PLAYER_DISTANCE
# SECOND_Y_END = FIRST_Y_END + PLAYER_DISTANCE
#
# THIRD_Y_START = SECOND_Y_START + PLAYER_DISTANCE - 1
# THIRD_Y_END = SECOND_Y_END + PLAYER_DISTANCE - 1
#
# FOURTH_Y_START = THIRD_Y_START + PLAYER_DISTANCE - 1
# FOURTH_Y_END = THIRD_Y_END + PLAYER_DISTANCE - 1
#
# FIFTH_Y_START = FOURTH_Y_START + PLAYER_DISTANCE
# FIFTH_Y_END = FOURTH_Y_END + PLAYER_DISTANCE
#
# SIXTH_Y_START = FIFTH_Y_START + PLAYER_DISTANCE
# SIXTH_Y_END = FIFTH_Y_END + PLAYER_DISTANCE
#
# SEVENTH_Y_START = SIXTH_Y_START + PLAYER_DISTANCE - 1
# SEVENTH_Y_END = SIXTH_Y_END + PLAYER_DISTANCE - 1
#
# EIGHTH_Y_START = SEVENTH_Y_START + PLAYER_DISTANCE - 1
# EIGHTH_Y_END = SEVENTH_Y_END + PLAYER_DISTANCE - 1
#
# X_COORDINATES_START = [FIRST_X_START, SECOND_X_START, THIRD_X_START, FOURTH_X_START, FIFTH_X_START, SIXTH_X_START, SEVENTH_X_START, EIGHTH_X_START, NINTH_X_START, TENTH_X_START]
# X_COORDINATES_END = [FIRST_X_END, SECOND_X_END, THIRD_X_END, FOURTH_X_END, FIFTH_X_END, SIXTH_X_END, SEVENTH_X_END, EIGHTH_X_END, NINTH_X_END, TENTH_X_END]
# Y_COORDINATES_START = [FIRST_Y_START, SECOND_Y_START, THIRD_Y_START, FOURTH_Y_START, FIFTH_Y_START, SIXTH_Y_START, SEVENTH_Y_START, EIGHTH_Y_START]
# Y_COORDINATES_END = [FIRST_Y_END, SECOND_Y_END, THIRD_Y_END, FOURTH_Y_END, FIFTH_Y_END, SIXTH_Y_END, SEVENTH_Y_END, EIGHTH_Y_END]
#
# LEVEL_ICON_HEIGHT = 7
# count3 = 0
# for i in range (0, 80):
#     if i%10 == 0:
#         count3 = 0 + int(i/10)
#
#     img = cv2.imread("G:/qwert.png")
#     grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     hero_level = ""
#     level_icon_template = grayed_img[Y_COORDINATES_END[count3] + 1:Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT, X_COORDINATES_START[i%10]:X_COORDINATES_END[i%10]]
#     for level in level_dict:
#         res = cv2.matchTemplate(level_dict[level], level_icon_template, cv2.TM_CCOEFF_NORMED)
#         if max(res) > 0.7:
#             hero_level = level
#             break
#
#     hero_icon_template = img[Y_COORDINATES_START[count3]:Y_COORDINATES_END[count3], X_COORDINATES_START[i%10]:X_COORDINATES_END[i%10]]
#     all_matches = []
#     for hero_name in namelist:
#         res = cv2.matchTemplate(hero_icon_dict[hero_name],hero_icon_template,cv2.TM_CCOEFF_NORMED)
#         loc = np.where(res >= 0.63)
#         if loc[0].size > 0:
#             all_matches.append((hero_name, max(res)))
#
#     all_matches = sorted(all_matches, key=lambda match: match[1])
#     if len(all_matches) > 0:
#         list_of_players[count3].append(all_matches[-1][0] + hero_level)
#
#
#
#
#
# print((list_of_players))



# template = cv2.imread("G:/asdff.png", 0)[Y_COORDINATES_START[count3]:Y_COORDINATES_END[count3], X_COORDINATES_START[0%10]:X_COORDINATES_END[0%10]]
# cv2.imshow("template", template)
# cv2.waitKey(0)


# count3 = 0
# i=2
# ystart = Y_COORDINATES_START[count3]
# yend = Y_COORDINATES_END[count3]
# xstart = X_COORDINATES_START[i%10]
# xend = X_COORDINATES_END[i % 10]
#
# template = cv2.imread("G:/asdff.png")[ystart: yend, xstart:xend]
# res = cv2.matchTemplate(hero_icon_dict["AA"],template,cv2.TM_CCOEFF_NORMED)
# loc = np.where(res >= 0.65)
# print(res)
# print(loc)
# plt2_image = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
# imgplot2 = plt.imshow(plt2_image)
# plt.show()
# # cv2.imshow("aba", des)
# plt_image = cv2.cvtColor(hero_icon_dict["Razor"], cv2.COLOR_BGR2RGB)
# imgplot = plt.imshow(plt_image)
# plt.show()

# print(res[loc[0][0]][loc[1][0]])
# print(max(res))
# os.chdir("G:/")
#




# a = (1705, 701)
# b = 1753, 712
# c = 875, 885

# img = cv2.imread("G:/ewq.png")[701:712, 1705:1754]
# os.chdir("G:/")
# cv2.imwrite("fac.png" ,img)

# constant = (312, 978)
# screenshot = cv2.imread("G:/ewq.png")
# player3_status = screenshot[438:449, 1705:1754]
# player4_status = screenshot[525:536, 1705:1754]
# player5_status = screenshot[613:624, 1705:1754]
# player6_status = screenshot[701:712, 1705:1754]
# player7_status = screenshot[788:799, 1705:1754]
# player8_status = screenshot[875:886, 1705:1754]
# player_status_list = [player3_status, player4_status, player5_status, player6_status, player7_status, player8_status]
#
# failed_icon = cv2.imread("G:/failed_icon.png")
# transparent_failed_icon = cv2.imread("G:/transparent_failed_icon.png")
#
# num_of_lost_players = 0
# for i in range(0, len(player_status_list)):
#     if max(cv2.matchTemplate(player_status_list[i],failed_icon,cv2.TM_CCOEFF_NORMED)) > 0.8 or max(cv2.matchTemplate(player_status_list[i],transparent_failed_icon,cv2.TM_CCOEFF_NORMED)) > 0.8:
#         num_of_lost_players = 6 - i
#         break

# os.chdir("G:/darknet/")
# os.system(
#     "G:\darknet/darknet.exe detector test G:\darknet/obj.data G:/darknet/thresh_cfg.cfg G:\darknetsave/yolov4-obj_last_25.weights -ext_output -dont_show -out G:/darknet/result.json < G:/darknet/data/train.txt")

# f = open("G:/darknet/result.json")
# data = json.load(f)
#
# for i in range(8):
#     for hero in data[i]["objects"]:
#         list_of_players[i].append(hero["name"])
#
#
# import pygetwindow as gw
# print(gw.getAllTitles())
# dota = gw.getWindowsWithTitle("aa")[0]
# dota.activate()


# import pygetwindow as gw
# import win32gui
# import autoit
# time.sleep(1)
# dota = gw.getWindowsWithTitle("Dota 2")[0]
# dota.activate()
# # for i in range(20):
# #     autoit.control_click("Dota 2", "",button="right",click=3,x=i*30,y=i*20)
# #     time.sleep(1)
# autoit.control_click("Dota 2", "",button="right",click=3,x=30,y=30)
# time.sleep(1)
# autoit.control_click("Dota 2", "",button="right",click=3,x=90,y=90)
# time.sleep(1)
# autoit.control_click("Dota 2", "",button="right",click=3,x=180,y=180)
# time.sleep(1)
# autoit.control_click("Dota 2", "",button="right",click=3,x=400,y=400)
# time.sleep(1)

# pyautogui.displayMousePosition()

# -*- coding: utf-8 -*-



# Pool_Dict = {}
#
# Pool_Dict = {'Barathum': ['Barathum', '1G', 'Chieftan', 'Assassin', 45], 'Axe': ['Axe', '1G', 'Orc', 'Warrior', 45], 'Enchantress': ['Enchantress', '1G', 'Beast', 'Druid', 45], 'Tuskar': ['Tuskar', '1G', 'Beast', 'Warrior', 45], 'Drow': ['Drow', '1G', 'Undead', 'Hunter', 45], 'BH': ['BH', '1G', 'Goblin', 'Assassin', 45], 'Clock': ['Clock', '1G', 'Goblin', 'Inventor', 45], 'ShadowShaman': ['ShadowShaman', '1G', 'Troll', 'Shaman', 45], 'Tinker': ['Tinker', '1G', 'Goblin', 'Inventor', 45], 'AM': ['AM', '1G', 'Elf', 'DemonHunter', 45], 'Tiny': ['Tiny', '1G', 'Elemental', 'Warrior', 45], 'Mars':
#  ['Mars', '1G', 'God', 'Warrior', 45], 'IceDuck': ['IceDuck', '1G', 'Dragon', 'Mage', 45], 'CM': ['CM', '1G', 'Human', 'Mage', 45], 'Luna': ['Luna', '1G', 'Elf', 'Knight', 45], 'WitchDoctor': ['WitchDoctor', '1G', 'Troll', 'Warlock', 45], 'Lion': ['Lion', '2G', 'Demon', 'Wizard', 30], 'Batrider': ['Batrider', '2G', 'Troll', 'Knight', 30], 'OgreMagi': ['OgreMagi', '2G', 'Ogre', 'Mage', 30
# ], 'BeastMaster': ['BeastMaster', '2G', 'Orc', 'Hunter', 30], 'Juggernaut': ['Juggernaut', '2G', 'Orc', 'Warrior', 30], 'Timber': ['Timber', '2G', 'Goblin', 'Inventor', 30], 'Chaos': ['Chaos', '2G', 'Demon', 'Knight', 30], 'Morph': ['Morph', '2G', 'Elemental', 'Assassin', 30], 'NP': ['NP', '2G', 'Elf', 'Druid', 30], 'Mirana': ['Mirana', '2G', 'Elf', 'Hunter', 30], 'Slark': ['Slark', '2G'
# , 'Naga', 'Assassin', 30], 'Dazzle': ['Dazzle', '2G', 'Troll', 'Priest', 30], 'Sniper': ['Sniper', '2G', 'Dwarf', 'Hunter', 30], 'Abaddon': ['Abaddon', '2G', 'Undead', 'Knight', 30], 'Oracle': ['Oracle', '2G', 'God', 'Priest', 30], 'Panda': ['Panda', '2G', 'Pandaren', 'Monk', 30], 'Venom': ['Venom', '3G', 'Aqir/Beast', 'Warlock', 25], 'OmniKnight': ['OmniKnight', '3G', 'Human', 'Knight', 25], 'Razor': ['Razor', '3G', 'Elemental', 'Mage', 25], 'PhuongAnh': ['PhuongAnh', '3G', 'Elf', 'Assassin', 25], 'Treant': ['Treant', '3G', 'Elf', 'Druid', 25], 'Sladar': ['Sladar', '3G', 'Naga', 'Warrior', 25], 'SandKing': ['SandKing', '3G', 'Aqir', 'Assassin', 25], 'Lycan': ['Lycan', '3G', 'Human/Beast', 'Warrior', 25], 'TB': ['TB', '3G', 'Demon', 'DemonHunter', 25], 'Viper': ['Viper', '3G', 'Dragon', 'Assassin', 25], 'Nevermore': ['Nevermore', '3G', 'Demon', 'Warlock', 25], 'LC': ['LC', '3G', 'Human', 'Knight', 25], 'Lina': ['Lina', '3G', 'Human', 'Mage', 25], 'Visage': ['Visage', '3G', 'Dragon/Undead', 'Hunter', 25], 'Rubik': ['Rubik', '3G', 'God', 'Wizard', 25], 'Meepo': ['Meepo', '3G', 'Kobold', 'Inventor', 25], 'WindRanger': ['WindRanger', '4G', 'Elf', 'Hunter', 15], 'Doom': ['Doom', '4G', 'Demon', 'Warrior', 15], 'Kunkka': ['Kunkka', '4G', 'Human', 'Warrior', 15], 'Grim': ['Grim', '4G', 'Demon', 'Wizard', 15], 'KOTL': ['KOTL', '4G', 'Human', 'Mage', 15], 'Necrophos': ['Necrophos', '4G', 'Undead', 'Warlock', 15], 'Alchemist': ['Alchemist', '4G', 'Goblin', 'Warlock', 15], 'DragonKnight': ['DragonKnight', '4G', 'Human/Dragon', 'Knight', 15], 'Medusa': ['Medusa', '4G', 'Naga', 'Hunter', 15], 'LD': ['LD', '4G', 'Beast', 'Druid', 15], 'Chen': ['Chen', '4G', 'Orc', 'Priest', 15], 'Nyx': ['Nyx', '4G', 'Aqir', 'Assassin', 15],
# 'Brood': ['Brood', '4G', 'Aqir', 'Hunter', 15], 'EarthShaker': ['EarthShaker', '4G', 'Chieftan', 'Shaman', 15], 'Disruptor': ['Disruptor', '5G', 'Orc', 'Shaman', 10], 'Gyro': ['Gyro', '5G', 'Dwarf', 'Inventor',10], 'Tide': ['Tide', '5G', 'Naga', 'Hunter', 10], 'Enigma': ['Enigma', '5G', 'Elemental', 'Warlock', 10], 'Terrorist': ['Terrorist', '5G', 'Goblin', 'Inventor', 10], 'Elder': ['Elder', '5G', 'God/Chieftan', 'Druid', 10], 'Sven': ['Sven', '5G', 'Demon', 'Warrior', 10], 'Zeus': ['Zeus', '5G', 'God', 'Mage', 10], 'QOP': ['QOP', '5G', 'Demon', 'Assassin', 10], 'TramAnh': ['TramAnh', '5G', 'Elf', 'Assassin', 10], 'MonkeyKing': ['MonkeyKing', '5G', 'Beast', 'Monk', 10], 'Invoker': ['Invoker', '5G', 'Elf', 'Mage', 10], 'Huskar': ['Huskar', '5G', 'Troll', 'Warrior', 10], 'Jakiro': ['Jakiro', '5G', 'Dragon', 'Mage', 10], 'Snapfire': ['Snapfire', '5G', 'Goblin', 'Knight', 10]}
#
#
# list_of_players[0].append("Axe")
# list_of_players[0].append("Barathum3")
# list_of_players[0].append("Enchantress2")
# for hero in list_of_players[0]:
#     if hero.endswith("2"):
#         Pool_Dict[hero[:-1]][4] -= 3
#     elif hero.endswith("3"):
#         Pool_Dict[hero[:-1]][4] -= 6
#     else:
#         Pool_Dict[hero][4] -= 1
#
# # a = "Enchantress2"
# # print(a[:-1])
# #
# import tkinter as tk
# from tkinter import ttk
# def OnDoubleClick(event):
#     item = treeview.selection()[0]
#     print(treeview.selection())
#     print(treeview.selection()[0])
#
#     print("you clicked on", treeview.item(item,"text"))
#
# def treeview_sort_column(treeview: ttk.Treeview, col, reverse: bool):
#     """
#     to sort the table by column when clicking in column
#     """
#     try:
#         data_list = [
#             (int(treeview.set(k, col)), k) for k in treeview.get_children("")
#         ]
#     except Exception:
#         data_list = [(treeview.set(k, col), k) for k in treeview.get_children("")]
#
#     data_list.sort(reverse=reverse)
#
#     # rearrange items in sorted positions
#     for index, (val, k) in enumerate(data_list):
#         treeview.move(k, "", index)
#
#     # reverse sort next time
#     treeview.heading(
#         column=col,
#         text=col,
#         command=lambda col3=col: treeview_sort_column(
#             treeview, col3, not reverse),)
#
# root = tk.Tk()
# columns = ['Rank', 'Species', 'Class', 'Name', 'Pool']
# # columns = ['name']
# treeview = ttk.Treeview(root, columns=columns, show='headings', height=30, selectmode="extended")
# for col in columns:
#     treeview.heading(col, text=col, anchor="w", command=lambda col3 = col:treeview_sort_column(treeview, col3, False))
# treeview.column('Rank', anchor='w', width=34)
# treeview.column('Species', anchor='w', width=93)
# treeview.column('Class', anchor='w', width=85)
# treeview.column('Name', anchor='w', width=93)
# treeview.column('Pool', anchor='w', width=34)
#
# count1 = 0
# for key in Pool_Dict:
#     treeview.insert(parent="", index='end', iid=count1, text='', values=(Pool_Dict[key][1], Pool_Dict[key][2], Pool_Dict[key][3], Pool_Dict[key][0], Pool_Dict[key][4]))
#     count1 +=1
#
# # treeview.insert(parent="", index='end', iid=0, text="", values=("john", 30))
#
# treeview.pack(fill="both",expand=1)
# tk.mainloop()
# #
#
# # print(Pool_Dict)
#
# print(list_of_players)


# import tkinter as tk
# import tkinter.ttk as ttk
#
# class App:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.tree = ttk.Treeview()
#         self.tree.pack()
#         for i in range(10):
#             self.tree.insert("", "end", text="Item %s" % i)
#         self.tree.bind("<Double-1>", self.OnDoubleClick)
#         self.root.mainloop()
#
#     def OnDoubleClick(self, event):
#         item = self.tree.selection()[0]
#         print("you clicked on", self.tree.item(item,"text"))
#
# if __name__ == "__main__":
#     app = App()

# !/usr/bin/python3

"""
tkentrycomplete.py
A tkinter widget that features autocompletion.
Created by Mitja Martini on 2008-11-29.
Converted to Python3 by Ian weisser on 2014-04-06.
Edited by Victor Domingos on 2016-04-25.
"""

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# columns = ['Rank', 'Species', 'Class', 'Name', 'Pool']
# # columns = ['name']
# treeview = ttk.Treeview(root, columns=columns, show='headings', height=30, selectmode="extended")
# for col in columns:
#     treeview.heading(col, text=col, anchor="w", command=lambda col3 = col:treeview_sort_column(treeview, col3, False))
# treeview.column('Rank', anchor='w', width=34)
# treeview.column('Species', anchor='w', width=93)
# treeview.column('Class', anchor='w', width=85)
# treeview.column('Name', anchor='w', width=93)
# treeview.column('Pool', anchor='w', width=34)
#
# # count1 = 0
# # for key in Pool_Dict:
# #     treeview.insert(parent="", index='end', iid=count1, text='', values=(Pool_Dict[key][1], Pool_Dict[key][2], Pool_Dict[key][3], Pool_Dict[key][0], Pool_Dict[key][4]))
# #     count1 +=1
#
# def comboclick(event):
#     mylabel = tk.Label(root,text=mycombo.get()).pack()
#
# mycombo = ttk.Combobox(root, value =['axe', 'magma', 'pikachu'] )
# mycombo.current(0)
# mycombo.bind("<<ComboboxSelected>>", comboclick)
# mycombo.pack()
#
#
#
# treeview.pack(fill="both",expand=1)
# tk.mainloop()

"""
Inspired by http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/
Changes:
    - Fixed AttributeError: 'AutocompleteEntry' object has no attribute 'listbox'
    - Fixed scrolling listbox
    - Case-insensitive search
    - Added focus to entry field
    - Custom listbox length, listbox width matches entry field width
    - Custom matches function
"""

"""
Inspired by http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/
Changes:
    - Fixed AttributeError: 'AutocompleteEntry' object has no attribute 'listbox'
    - Fixed scrolling listbox
    - Case-insensitive search
    - Added focus to entry field
    - Custom listbox length, listbox width matches entry field width
    - Custom matches function
"""

"""
changes made:
    make widgets parent explicitly declared
    Use either with root window or Toplevel
    Bind Return key to selection method
"""

#from tkinter import *
# import tkinter as tk
# import re
#
#
# class AutocompleteEntry(tk.Entry):
#     def __init__(self, autocompleteList, *args, **kwargs):
#
#         self.listboxLength = 0
#         self.parent = args[0]
#
#         # Custom matches function
#         if 'matchesFunction' in kwargs:
#             self.matchesFunction = kwargs['matchesFunction']
#             del kwargs['matchesFunction']
#         else:
#             def matches(fieldValue, acListEntry):
#                 pattern = re.compile(
#                     '.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
#                 return re.match(pattern, acListEntry)
#
#             self.matchesFunction = matches
#
#         # Custom return function
#         if 'returnFunction' in kwargs:
#             self.returnFunction = kwargs['returnFunction']
#             del kwargs['returnFunction']
#         else:
#             def selectedValue(value):
#                 print(value)
#             self.returnFunction = selectedValue
#
#         tk.Entry.__init__(self, *args, **kwargs)
#         #super().__init__(*args, **kwargs)
#         self.focus()
#
#         self.autocompleteList = autocompleteList
#
#         self.var = self["textvariable"]
#         if self.var == '':
#             self.var = self["textvariable"] = tk.StringVar()
#
#         self.var.trace('w', self.changed)
#         self.bind("<Right>", self.selection)
#         self.bind("<Up>", self.moveUp)
#         self.bind("<Down>", self.moveDown)
#         self.bind("<Return>", self.selection)
#         self.bind("<Escape>", self.deleteListbox)
#
#         self.listboxUp = False
#
#     def deleteListbox(self, event=None):
#         if self.listboxUp:
#             self.listbox.destroy()
#             self.listboxUp = False
#
#     def select(self, event=None):
#         if self.listboxUp:
#             index = self.listbox.curselection()[0]
#             value = self.listbox.get(tk.ACTIVE)
#             self.listbox.destroy()
#             self.listboxUp = False
#             self.delete(0, tk.END)
#             self.insert(tk.END, value)
#             self.returnFunction(value)
#
#     def changed(self, name, index, mode):
#         if self.var.get() == '':
#             self.deleteListbox()
#         else:
#             words = self.comparison()
#             if words:
#                 if not self.listboxUp:
#                     self.listboxLength = len(words)
#                     self.listbox = tk.Listbox(self.parent,
#                         width=self["width"], height=self.listboxLength)
#                     self.listbox.bind("<Button-1>", self.selection)
#                     self.listbox.bind("<Right>", self.selection)
#                     self.listbox.place(
#                         x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
#                     self.listboxUp = True
#                 else:
#                     self.listboxLength = len(words)
#                     self.listbox.config(height=self.listboxLength)
#
#                 self.listbox.delete(0, tk.END)
#                 for w in words:
#                     self.listbox.insert(tk.END, w)
#             else:
#                 self.deleteListbox()
#
#     def selection(self, event):
#         if self.listboxUp:
#             self.var.set(self.listbox.get(tk.ACTIVE))
#             self.listbox.destroy()
#             self.listboxUp = False
#             self.icursor(tk.END)
#
#     def moveUp(self, event):
#         if self.listboxUp:
#             if self.listbox.curselection() == ():
#                 index = '0'
#             else:
#                 index = self.listbox.curselection()[0]
#
#             self.listbox.selection_clear(first=index)
#             index = str(int(index) - 1)
#             if int(index) == -1:
#                 index = str(self.listboxLength-1)
#
#             self.listbox.see(index)  # Scroll!
#             self.listbox.selection_set(first=index)
#             self.listbox.activate(index)
#
#     def moveDown(self, event):
#         if self.listboxUp:
#             if self.listbox.curselection() == ():
#                 index = '-1'
#             else:
#                 index = self.listbox.curselection()[0]
#
#             if index != tk.END:
#                 self.listbox.selection_clear(first=index)
#                 if int(index) == self.listboxLength-1:
#                     index = "0"
#                 else:
#                     index = str(int(index)+1)
#
#                 self.listbox.see(index)  # Scroll!
#                 self.listbox.selection_set(first=index)
#                 self.listbox.activate(index)
#
#     def comparison(self):
#         return [w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w)]

# from tkinter import ttk
#
# if __name__ == '__main__':
#     autocompleteList = ['Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)', 'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)', 'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)', 'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)', 'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)', 'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)', 'Melodie Wooten (7753)', 'Winter Beard (3896)', 'Callum Schultz (7762)', 'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)', 'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)', 'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)', 'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)', 'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)', 'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)', 'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)', 'Marah Odonnell (3115)',
#                         'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)', 'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)', 'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)', 'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)', 'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)', 'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)', 'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)', 'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)', 'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)', 'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)', 'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)', 'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)', 'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)', 'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)', 'Talon Winters (8469)']
#
#     def matches(fieldValue, acListEntry):
#         pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
#         return re.match(pattern, acListEntry)
#
#     style = ttk.Style()
#
#     root = tk.Tk()
#     topLevel = tk.Toplevel()
#     topLevel.title('TopLevel')
#     #pass either root or toplevel as the second argument to use as entry's parent widget
#     entry = AutocompleteEntry(
#         autocompleteList, root, width=32, matchesFunction=matches)
#     entry.grid(row=0, column=0)
#     tk.Button(topLevel, text='Python').grid(column=0)
#     tk.Button(topLevel, text='Tkinter').grid(column=0)
#     tk.Button(topLevel, text='Regular Expressions').grid(column=0)
#     tk.Button(topLevel, text='Fixed bugs').grid(column=0)
#     tk.Button(topLevel, text='New features').grid(column=0)
#     tk.Button(topLevel, text='Check code comments').grid(column=0)
#     root.mainloop()

# from PyQt5.QtWidgets import *
# from PyQt5.Qt import Qt
# from PyQt5 import QtGui
# from PyQt5.QtCore import QVariant
# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtCore import QVariantAnimation, QEasingCurve, QEventLoop, QTimer
# from PyQt5.QtGui import QColor, QPalette
# import sys

# class AnimationLabel(QLabel):
#     def __init__(self, *args, **kwargs):
#         QLabel.__init__(self, *args, **kwargs)
#         self.animation = QVariantAnimation()
#         self.animation.valueChanged.connect(self.changeColor)
#
#     @pyqtSlot(QVariant)
#     def changeColor(self, color):
#         palette = self.palette()
#         palette.setColor(QPalette.WindowText, color)
#         self.setPalette(palette)
#
#     def startFadeIn(self):
#         self.animation.stop()
#         self.animation.setStartValue(QColor(0, 0, 0, 0))
#         self.animation.setEndValue(QColor(0, 0, 0, 255))
#         self.animation.setDuration(2000)
#         self.animation.setEasingCurve(QEasingCurve.InBack)
#         self.animation.start()
#
#     def startFadeOut(self):
#         self.animation.stop()
#         self.animation.setStartValue(QColor(0, 0, 0, 255))
#         self.animation.setEndValue(QColor(0, 0, 0, 0))
#         self.animation.setDuration(2000)
#         self.animation.setEasingCurve(QEasingCurve.OutBack)
#         self.animation.start()
#
#     def startAnimation(self):
#         self.startFadeIn()
#         loop = QEventLoop()
#         self.animation.finished.connect(loop.quit)
#         loop.exec_()
#         QTimer.singleShot(2000, self.startFadeOut)
#
# class Widget(QWidget):
#     def __init__(self):
#         super().__init__()
#         lay = QVBoxLayout(self)
#         self.greeting_text = AnimationLabel("greeting_text")
#         self.greeting_text.setStyleSheet("font : 45px; font : bold; font-family : HelveticaNeue-UltraLight")
#         lay.addWidget(self.greeting_text)
#         btnFadeIn = QPushButton("fade in")
#         btnFadeOut = QPushButton("fade out")
#         btnAnimation = QPushButton("animation")
#         lay.addWidget(btnFadeIn)
#         lay.addWidget(btnFadeOut)
#         lay.addWidget(btnAnimation)
#         btnFadeIn.clicked.connect(self.greeting_text.startFadeIn)
#         btnFadeOut.clicked.connect(self.greeting_text.startFadeOut)
#         btnAnimation.clicked.connect(self.greeting_text.startAnimation)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Widget()
#     ex.show()
#     sys.exit(app.exec_())
#
# from PyQt5 import QtCore, QtWidgets
# from random import choice
# from string import ascii_lowercase

# class TableSearch(QtWidgets.QTableWidget):
#     def __init__(self):
#         super().__init__(0, 3)
#         self.setEditTriggers(self.NoEditTriggers)
#         for row in range(500):
#             self.insertRow(row)
#             for col in range(3):
#                 text = ''.join(choice(ascii_lowercase) for i in range(5))
#                 self.setItem(row, col, QtWidgets.QTableWidgetItem(text))
#
#         self.searchWidget = QtWidgets.QLabel(self)
#         self.searchWidget.setStyleSheet('''
#             QLabel {
#                 border: 1px inset darkGray;
#                 border-radius: 2px;
#                 background: palette(window);
#             }
#             ''')
#         self.searchWidget.hide()
#         self.searchTimer = QtCore.QTimer(
#             singleShot=True,
#             timeout=self.resetSearch,
#             interval=QtWidgets.QApplication.instance().keyboardInputInterval())
#
#     def resetSearch(self):
#         self.searchWidget.setText('')
#         self.searchWidget.hide()
#
#     def updateSearchWidget(self):
#         if not self.searchWidget.text():
#             self.searchWidget.hide()
#             return
#         self.searchWidget.show()
#         self.searchWidget.adjustSize()
#         geo = self.searchWidget.geometry()
#         geo.moveBottomRight(
#             self.viewport().geometry().bottomRight() - QtCore.QPoint(2, 2))
#         self.searchWidget.setGeometry(geo)
#
#     def keyboardSearch(self, search):
#         super().keyboardSearch(search)
#         if not search:
#             self.searchWidget.setText('')
#         else:
#             text = self.searchWidget.text()
#             if not text:
#                 text = 'Searching: '
#             text += search
#             self.searchWidget.setText(text)
#         self.updateSearchWidget()
#         self.searchTimer.start()
#
#     def resizeEvent(self, event):
#         super().resizeEvent(event)
#         self.updateSearchWidget()


# QShortcut(Qt.Key_Q, self, activated=lambda: self.keyPressEvent("q"))
# QShortcut(Qt.Key_W, self, activated=lambda: self.keyPressEvent("w"))
# QShortcut(Qt.Key_E, self, activated=lambda: self.keyPressEvent("e"))
# QShortcut(Qt.Key_R, self, activated=lambda: self.keyPressEvent("r"))
# QShortcut(Qt.Key_T, self, activated=lambda: self.keyPressEvent("t"))
# QShortcut(Qt.Key_Y, self, activated=lambda: self.keyPressEvent("y"))
# QShortcut(Qt.Key_U, self, activated=lambda: self.keyPressEvent("u"))
# QShortcut(Qt.Key_I, self, activated=lambda: self.keyPressEvent("i"))
# QShortcut(Qt.Key_O, self, activated=lambda: self.keyPressEvent("o"))
# QShortcut(Qt.Key_P, self, activated=lambda: self.keyPressEvent("p"))
# QShortcut(Qt.Key_A, self, activated=lambda: self.keyPressEvent("a"))
# QShortcut(Qt.Key_S, self, activated=lambda: self.keyPressEvent("s"))
# QShortcut(Qt.Key_D, self, activated=lambda: self.keyPressEvent("d"))
# QShortcut(Qt.Key_F, self, activated=lambda: self.keyPressEvent("f"))
# QShortcut(Qt.Key_G, self, activated=lambda: self.keyPressEvent("g"))
# QShortcut(Qt.Key_H, self, activated=lambda: self.keyPressEvent("h"))
# QShortcut(Qt.Key_J, self, activated=lambda: self.keyPressEvent("j"))
# QShortcut(Qt.Key_K, self, activated=lambda: self.keyPressEvent("k"))
# QShortcut(Qt.Key_L, self, activated=lambda: self.keyPressEvent("l"))
# QShortcut(Qt.Key_Z, self, activated=lambda: self.keyPressEvent("z"))
# QShortcut(Qt.Key_X, self, activated=lambda: self.keyPressEvent("x"))
# QShortcut(Qt.Key_C, self, activated=lambda: self.keyPressEvent("c"))
# QShortcut(Qt.Key_V, self, activated=lambda: self.keyPressEvent("v"))
# QShortcut(Qt.Key_B, self, activated=lambda: self.keyPressEvent("b"))
# QShortcut(Qt.Key_N, self, activated=lambda: self.keyPressEvent("n"))
# QShortcut(Qt.Key_M, self, activated=lambda: self.keyPressEvent("m"))

# namelist = (
#     'AA',
#     'Abaddon',
#     'Alchemist',
#     'AM',
#     'Arc',
#     'Axe',
#     'Bane',
#     'Barathum',
#     'Batrider',
#     'BB',
#     'BeastMaster',
#     'BH',
#     'Blood',
#     'Brood',
#     'Centaur',
#     'Chaos',
#     'Chen',
#     'Clinkz',
#     'Clock',
#     'CM',
#     'DarkWillow',
#     'Dazzle',
#     'Disruptor',
#     'Doom',
#     'DP',
#     'DragonKnight',
#     'Drow',
#     'DS',
#     'EarthShaker',
#     'EarthSpirit',
#     'Elder',
#     'EmberSpirit',
#     'Enchantress',
#     'Enigma',
#     'Grandma',
#     'Grim',
#     'Gyro',
#     'Huskar',
#     'IceDuck',
#     'Invoker',
#     'IO',
#     'Jakiro',
#     'Juggernaut',
#     'KOTL',
#     'Kunkka',
#     'LC',
#     'LD',
#     'Leshrac',
#     'Lich',
#     'Lina',
#     'Lion',
#     'Luna',
#     'Lycan',
#     'Magnus',
#     'Mars',
#     'Medusa',
#     'Meepo',
#     'Mirana',
#     'MonkeyKing',
#     'Morph',
#     'Naga',
#     'Naix',
#     'Necrophos',
#     'Nevermore',
#     'NP',
#     'NS',
#     'Nyx',
#     'OD',
#     'OgreMagi',
#     'OmniKnight',
#     'Oracle',
#     'Panda',
#     'Pangolier',
#     'Phoenix',
#     'PhuongAnh',
#     'PhuongLinh',
#     'Puck',
#     'Pudge',
#     'Pugna',
#     'QOP',
#     'Razor',
#     'Riki',
#     'Rubik',
#     'SandKing',
#     'SD',
#     'ShadowShaman',
#     'Silencer',
#     'SkeletonKing',
#     'SkywrathMage',
#     'Sladar',
#     'Slark',
#     'Sniper',
#     'Spectre',
#     'Storm',
#     'Sven',
#     'TB',
#     'Terrorist',
#     'Tide',
#     'Timber',
#     'Tinker',
#     'Tiny',
#     'TramAnh',
#     'Treant',
#     'Troll',
#     'Tuskar',
#     'Underlord',
#     'Undying',
#     'Ursa',
#     'Venom',
#     'Viper',
#     'Visage',
#     'Void',
#     'VoidSpirit',
#     'VS',
#     'Warlock',
#     'Weaver',
#     'WindRanger',
#     'WitchDoctor',
#     'WraithKing',
#     'Zeus'
# )
#
# import nltk
#
# a = """
# Assassin
#
# Aqir
#
#
# DemonHunter
#
#
# Druid
#
# Hunter
#
#
# Knight
#
#
#
#
# Mage
#
#
# Inventor
#
#
# Priest
#
# Shaman
#
#
# Warlock
#
#
# Warrior
#
#
#
# Wizard
#
#
# Dragon
#
#
# Dwarf
#
#
# Demon
#
#
# Ogre
#
#
# Elf
#
#
# Undead
#
# Orc
#
#
# Goblin
#
# Elemental
#
# Razor
#
# Enigma
#
# Human
#
# Naga
#
# Troll
#
#
# Beast
#
#
# God
#
# Kobold
#
# """

# b = ['Assassin', 'Aqir', 'DemonHunter', 'Druid', 'Hunter', 'Knight', 'Mage', 'Inventor', 'Priest', 'Shaman', 'Warlock', 'Warrior', 'Wizard', 'Dragon', 'Dwarf', 'Demon', 'Ogre', 'Elf', 'Undead', 'Orc', 'Goblin', 'Elemental', 'Razor', 'Enigma', 'Human', 'Naga', 'Troll', 'Beast', 'God', 'Kobold', 'AA', 'Abaddon', 'Alchemist', 'AM', 'Arc', 'Axe', 'Bane', 'Barathum', 'Batrider', 'BB', 'BeastMaster', 'BH', 'Blood', 'Brood', 'Centaur', 'Chaos', 'Chen', 'Clinkz', 'Clock', 'CM', 'DarkWillow', 'Dazzle', 'Disruptor', 'Doom', 'DP', 'DragonKnight', 'Drow', 'DS', 'EarthShaker', 'EarthSpirit', 'Elder', 'EmberSpirit', 'Enchantress', 'Enigma', 'Grandma', 'Grim', 'Gyro', 'Huskar', 'IceDuck', 'Invoker', 'IO', 'Jakiro', 'Juggernaut', 'KOTL', 'Kunkka', 'LC', 'LD', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Luna', 'Lycan', 'Magnus', 'Mars', 'Medusa', 'Meepo', 'Mirana', 'MonkeyKing', 'Morph', 'Naga', 'Naix', 'Necrophos', 'Nevermore', 'NP', 'NS', 'Nyx', 'OD', 'OgreMagi', 'OmniKnight', 'Oracle', 'Panda', 'Pangolier', 'Phoenix', 'PhuongAnh', 'PhuongLinh', 'Puck', 'Pudge', 'Pugna', 'QOP', 'Razor', 'Riki', 'Rubik', 'SandKing', 'SD', 'ShadowShaman', 'Silencer', 'SkeletonKing', 'SkywrathMage', 'Sladar', 'Slark', 'Sniper', 'Spectre', 'Storm', 'Sven', 'TB', 'Terrorist', 'Tide', 'Timber', 'Tinker', 'Tiny', 'TramAnh', 'Treant', 'Troll', 'Tuskar', 'Underlord', 'Undying', 'Ursa', 'Venom', 'Viper', 'Visage', 'Void', 'VoidSpirit', 'VS', 'Warlock', 'Weaver', 'WindRanger', 'WitchDoctor', 'WraithKing', 'Zeus']

# classandspecies = ('Assassin', 'Aqir', 'DemonHunter', 'Druid', 'Hunter', 'Knight', 'Mage', 'Inventor', 'Priest', 'Shaman', 'Warlock', 'Warrior', 'Wizard', 'Dragon', 'Dwarf', 'Demon', 'Ogre', 'Elf', 'Undead', 'Orc', 'Goblin', 'Elemental', 'Razor', 'Enigma', 'Human', 'Naga', 'Troll', 'Beast', 'God', 'Kobold')
#
# b = namelist+classandspecies
# print(b)
#
# f = open("C:/autochess_data/Strategies.txt","w")
#
# for item in b:
#
#     f.write("# (cat) " + item + ":")
#     f.write("\n")
#     f.write("- Hero's strengths")
#     f.write("\n")
#     f.write("- Hero's weaknesses")
#     f.write("\n")
#     f.write("- Hero counters")
#     f.write("\n")
#     f.write("- Hero's countered by")
#     f.write("> TODO\n")

# c = ['Assassin', 'Aqir', 'DemonHunter', 'Druid', 'Hunter', 'Knight', 'Mage', 'Inventor', 'Priest', 'Shaman', 'Warlock',
# 'Warrior', 'Wizard', 'Dragon', 'Dwarf', 'Demon', 'Ogre', 'Elf', 'Undead', 'Orc', 'Goblin', 'Elemental', 'Razor', 'Enigma', 'Human', 'Naga', 'Troll', 'Beast', 'God', 'Kobold']
import requests
import base64

# def push_to_github(filename, repo, branch, token):
#     url="https://api.github.com/repos/"+repo+"/contents/"+filename
#
#     base64content=base64.b64encode(open(filename,"rb").read())
#
#     data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
#     sha = data['sha']
#
#     if base64content.decode('utf-8')+"\n" != data['content']:
#         message = json.dumps({"message":"update",
#                             "branch": branch,
#                             "content": base64content.decode("utf-8") ,
#                             "sha": sha
#                             })
#
#         resp=requests.put(url, data = message, headers = {"Content-Type": "application/json", "Authorization": "token "+token})
#
#         print(resp)
#     else:
#         print("nothing to update")
import http
#
# token = "d77e1404d42233a084c3c377a73ceb3dbf00ced7"
# filename="Strategies.txt"
# repo = "Michael-Evergreen/auto_chess"
# branch="main"
# message = "abc"
# # push_to_github(filename, repo, branch, token)
# url = "https://api.github.com/repos/Michael-Evergreen/"
# resp = requests.post(url, data=message, headers={"Content-Type": "application/json", "Authorization": "token " + token})


#
# resp = requests.put("https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/hello.txt", headers={"Authorization: token d77e1404d42233a084c3c377a73ceb3dbf00ced7"})
# print(resp)

# r = requests.get('https://api.github.com/events')
# print(r.text)
# http PUT https://api.github.com/repos/lee-dohm/test-repo/contents/hello.txt \
#   "Authorization: token REDACTED-TOKEN" \
#   message="my commit message" \
#   committer="{ \"name\": \"Lee Dohm\", \"email\": \"1038121+lee-dohm@users.noreply.github.com\" }" \
#   content="bXkgbmV3IGZpbGUgY29udGVudHM="

import requests
import base64
import json
import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette, QFont, QTextCursor
import sys
from string import ascii_lowercase

# def push_to_repo_branch(gitHubFileName, fileName, repo_slug, branch, user, token):
#     '''
#     Push file update to GitHub repo
#
#     :param gitHubFileName: the name of the file in the repo
#     :param fileName: the name of the file on the local branch
#     :param repo_slug: the github repo slug, i.e. username/repo
#     :param branch: the name of the branch to push the file to
#     :param user: github username
#     :param token: github user token
#     :return None
#     :raises Exception: if file with the specified name cannot be found in the repo
#     '''
#
#     message = "Automated update " + str(datetime.datetime.now())
#     path = "https://api.github.com/repos/%s/branches/%s" % (repo_slug, branch)
#
#     r = requests.get(path, auth=(user, token))
#     if not r.ok:
#         print("Error when retrieving branch info from %s" % path)
#         print("Reason: %s [%d]" % (r.text, r.status_code))
#         raise
#     rjson = r.json()
#     treeurl = rjson['commit']['commit']['tree']['url']
#     r2 = requests.get(treeurl, auth=(user, token))
#     if not r2.ok:
#         print("Error when retrieving commit tree from %s" % treeurl)
#         print("Reason: %s [%d]" % (r2.text, r2.status_code))
#         raise
#     r2json = r2.json()
#     sha = None
#
#     for file in r2json['tree']:
#         # Found file, get the sha code
#         if file['path'] == gitHubFileName:
#             sha = file['sha']
#
#     # if sha is None after the for loop, we did not find the file name!
#     if sha is None:
#         print
#         "Could not find " + gitHubFileName + " in repos 'tree' "
#         raise Exception
#
#     with open(fileName) as data:
#         content = base64.b64encode(data.read())
#
#     # gathered all the data, now let's push
#     inputdata = {}
#     inputdata["path"] = gitHubFileName
#     inputdata["branch"] = branch
#     inputdata["message"] = message
#     inputdata["content"] = content
#     if sha:
#         inputdata["sha"] = str(sha)
#
#     updateURL = "https://api.github.com/repos/EBISPOT/RDF-platform/contents/" + gitHubFileName
#     try:
#         rPut = requests.put(updateURL, auth=(user, token), data=json.dumps(inputdata))
#         if not rPut.ok:
#             print("Error when pushing to %s" % updateURL)
#             print("Reason: %s [%d]" % (rPut.text, rPut.status_code))
#             raise Exception
#     except requests.exceptions.RequestException as e:
#         print()
        # print
        # 'Something went wrong! I will print all the information that is available so you can figure out what happend!'
        # print
        # rPut
        # print
        # rPut.headers
        # print
        # rPut.text


# path = "https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt"
# user = "Michael-Evergreen"
# token = "10c025f6982de29bae3d60e51760f0863a79bb78"
#
# r = requests.get(path, auth=(user, token))
# if not r.ok:
#     print("Error when retrieving branch info from %s" % path)
#     print("Reason: %s [%d]" % (r.text, r.status_code))
#
# sha = r.json()['sha']
#
# content = ""
# with open("C:/autochess_data/Strategies.txt", "r") as data:
#     datautf = data.read().encode("utf-8")
#     datab64 = base64.b64encode(datautf)
#     b64string = datab64.decode("utf-8")
#     # print(type(b64string))
#     # content = str(data)[1:]
#     content = b64string
# # print(data)
# # print(content)
# inputdata = {}
# inputdata["path"] = "https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt"
# inputdata["branch"] = "main"
# inputdata["message"] = "abc"
# inputdata["content"] = content
# inputdata["sha"] = sha
#
# try:
#     rPut = requests.put("https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt", auth=(user, token), data=json.dumps(inputdata))
#     if not rPut.ok:
#         print("Error when pushing to %s")
#         print("Reason: %s [%d]" % (rPut.text, rPut.status_code))
#         raise Exception
# except requests.exceptions.RequestException as e:
#     print(rPut)
#     print(rPut.headers)
#     print(rPut.text)



# print(rjson)
# treeurl = rjson['commit']['commit']['tree']['url']

# r2 = requests.get(treeurl, auth=(user, token))
# if not r2.ok:

# img_rgb = cv2.imread("G:/on_stage_chesspieces.png")
# template = cv2.imread("G:/Knight.png")
# # w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
#
# a = img_rgb[488+25:488+25+12, 1136+2:1136+19]
import sys

FIRST = 1136
SECOND = 1169
THIRD = 1202
FOURTH = 1235
FIFTH = 1268
SIXTH = 1301

SECONDY = 314

# name = sys.argv[1]
# print(name)
#
# # for pt in zip(*loc[::-1]):
# # img_rgb = cv2.imread("G:/on_stage_chesspieces.png")
# # a = img_rgb[SECONDY:SECONDY+25, FOURTH:FOURTH+25]
# # cv2.imwrite("G:/" + name + ".png", a)
# # b = img_rgb[751+25:751+25+12, 1136+2:1136+19]
# # cv2.imwrite("G:/3.png", b)
#
# img = cv2.imread("G:/Warrior.png")
# cv2.imshow("as", img)
# cv2.waitKey(0)

# CAS_numbers = [int(file[:-4]) for file in os.listdir("C:/autochess_data/class_species_numbers/") if file.endswith("png")]
# CAS_number_icons = [cv2.imread("C:/autochess_data/class_species_numbers/"+ file, 0) for file in os.listdir("C:/autochess_data/class_species_numbers/") if file.endswith("png")]
# CAS_numbers_and_icons = tuple(zip(CAS_numbers, CAS_number_icons))
#
# CAS_names = [file[:-4] for file in os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
# CAS_icons = [cv2.imread("C:/autochess_data/class_species_icons/"+ file) for file in os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
# CAS_names_and_icons = tuple(zip(CAS_names, CAS_icons))
#
# CAS_dict = {'Aqir': [0, 0], 'Assassin': [0, 0], 'Beast': [0, 0], 'Chieftan': [0, 0], 'Demon': [0, 0], 'Dragon': [0, 0], 'Druid': [0, 0], 'Dwarf': [0, 0], 'Elemental': [0, 0], 'Elf': [0, 0], 'Faceless': [0, 0], 'Goblin': [0, 0], 'God': [0, 0], 'Human': [0, 0], 'Hunter': [0, 0], 'Inventor': [0, 0], 'Knight': [0, 0], 'Kobold': [0, 0], 'Mage': [0, 0], 'Monk': [0, 0], 'Naga': [0, 0], 'Ogre': [0, 0], 'Orc': [0, 0], 'Pandaren': [0, 0], 'Priest': [0, 0], 'Shaman': [0, 0], 'Troll': [0, 0], 'Undead': [0, 0], 'Warlock': [0, 0], 'Warrior': [0, 0], 'Wizard': [0, 0]}
#
# unused_CAS = []
#
# #     print(CAS_names_and_icons[i][0])
# #     show(CAS_names_and_icons[i][1])
#
# on_stage_CAS_x_coors = (1136,1327)
# on_stage_CAS_y_coors = ((202, 289), (202, 373), (202, 460), (202, 547), (202, 635), (202, 723), (202, 810), (202, 897))
#
# on_stage_heroes = cv2.imread("C:/autochess_data/on_stage_heroes.png")
#
# num_of_lost_players = 0
# on_stage_CAS_icons = on_stage_heroes[
#     on_stage_CAS_y_coors[7-num_of_lost_players][0]:on_stage_CAS_y_coors[7-num_of_lost_players][1],
#     on_stage_CAS_x_coors[0]:on_stage_CAS_x_coors[1]]
# on_stage_CAS_icons_grayed = cv2.cvtColor(on_stage_CAS_icons, cv2.COLOR_BGR2GRAY)
# img = []
# for CAS in CAS_names_and_icons:
#     result = cv2.matchTemplate(on_stage_CAS_icons, CAS[1], cv2.TM_CCOEFF_NORMED)
#     loc = np.where(result >= 0.9)
#     if loc[0].size == 0:
#         unused_CAS.append(CAS[0])
#     else:
#         CAS_dict[CAS[0]][0] = loc[0].size
#         for i in range(loc[0].size):
#             number_icon = on_stage_CAS_icons_grayed[loc[0][i]+25:loc[0][i]+37, loc[1][i]+2:loc[1][i]+19]
#             result_list = []
#             for icon in CAS_numbers_and_icons:
#                 if cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED) > 0.85:
#                     result_list.append((icon[0], cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED)))
#             result_list = sorted(result_list, key=lambda icon: icon[1], reverse=True)
#             CAS_dict[CAS[0]][1] += result_list[0][0]


                    # CAS_dict[CAS[0]][1] += icon[0]
                    # break

# print(CAS_dict)
# number1 = on_stage_CAS_icons[112+25:112+37, 66+2:66+19]
# number11 = CAS_numbers_and_icons[0][1]
# cv2.imshow("number11", number11)
# cv2.imshow("number1", number1)
# cv2.imwrite("G:/1.png", number1)
# cv2.imwrite("G:/11.png", number11)
# # cv2.waitKey(0)
# # print(CAS_dict)


# print(loc[0][0])
# print(np.unravel_index(result.argmax(), result.shape))

from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
#
# class MyTableWidgetItem(QTableWidgetItem):
#     def __lt__(self, other):
#         if ( isinstance(other, QTableWidgetItem) ):
#             my_value, my_ok = self.data(Qt.EditRole).toInt()
#             other_value, other_ok = other.data(Qt.EditRole).toInt()
#
#             if ( my_ok and other_ok ):
#                 return my_value < other_value
#
#         return super(MyTableWidgetItem, self).__lt__(other)
#
# if ( __name__ == '__main__' ):
#     app = None
#     if ( QApplication.instance() is None ):
#         app = QApplication([])
#
#     widget = QTableWidget()
#     widget.setWindowFlags(Qt.Dialog)
#     widget.setSortingEnabled(True)
#
#     widget.setRowCount(50)
#     widget.setColumnCount(3)
#     for row in range(50):
#        # create a normal QTableWidgetItem
#        a = QTableWidgetItem()
#        a.setText(str(row))
#        widget.setItem(row, 0, a)
#
#        # create a proper sorted item
#        b = QTableWidgetItem()
#        b.setData(Qt.EditRole, QVariant(row))
#        widget.setItem(row, 1, b)
#
#        # create a custom sorted item
#        c = MyTableWidgetItem()
#        c.setData(Qt.EditRole, QVariant(row))
#        widget.setItem(row, 2, c)
#
#     widget.show()
#     if ( app ):
#         app.exec_()

from PyQt5.QtCore import Qt

# class MyProgressBar(QProgressBar):
#     def __init__(self):
#         super().__init__()
#         self.setRange(0, 0)
#         self.setAlignment(Qt.AlignCenter)
#         self._text = None
#
#     def setText(self, text):
#         self._text = text
#
#     def text(self):
#         return self._text
#
# app = QApplication([])
#
# p = MyProgressBar()
# p.setText('finding resource...')
# p.show()
#
# app.exec_()
# user = "Michael-Evergreen"
# token = "10c025f6982de29bae3d60e51760f0863a79bb78"
# rGet = requests.get("https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt", auth=(user, token))
# print(rGet.text)

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog
import re
import json
import os
import pyautogui
import time
import cv2
import numpy as np
import keyboard
import pygetwindow as gw
import threading
import copy
import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy
import requests
import base64
#

TIMESLEEP = 0.6

def thread(function, arg=None):
    if arg == None:
        x = threading.Thread(target=function)
        x.start()
    else:
        x = threading.Thread(target=function(arg))
        x.start()

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.UiC()

    def UiC(self):
        self.scan_button = QPushButton("Scan", self)
        self.scan_button.clicked.connect(self.Scan)
        # self.scan_button.clicked.connect(lambda state, x=self.Scan: thread(self.Scan))
        self.scan_button.move(0,0)

        self.progressbar = QProgressBar()
        self.progressbar.setRange(0, 0)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setFixedSize(700,500)
        self.progressbar.move(800, 20)

class WorkerThread(QThread):

def Scan():

        #
        # self.progressbar.setText("assdsa...")

        #
        # global to_show_list
        # to_show_list = all_chess_pieces_list
        # global on_stage_list
        # on_stage_list = temp_on_stage_list
        # print(temp_on_stage_list)

App = QApplication(sys.argv)


window = Myapp()
window.show()


sys.exit(App.exec())
