from tkinter import *
import re
from tkinter import ttk
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

"""
Load Strategies_and_Tips data from github  
"""
# user = "Michael-Evergreen"
# token = "10c025f6982de29bae3d60e51760f0863a79bb78"
# rGet = requests.get("https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt", auth=(user, token))
# data = (base64.b64decode(rGet.json()['content']).decode("utf-8"))
# with open("C:/autochess_data/Strategies.txt", "w") as f:
#     f.write(data)

"""
LOADS DATA AND CONSTANT VARIABLES TO RAM
"""

try:
    os.mkdir("C:/autochess_data")
except OSError as error:
    pass

namelist = (
    # 'AA',
    'Abaddon',
    'Alchemist',
    'AM',
    # 'Arc',
    'Axe',
    # 'Bane',
    'Barathum',
    'Batrider',
    # 'BB',
    'BeastMaster',
    'BH',
    # 'Blood',
    'Brood',
    # 'Centaur',
    'Chaos',
    'Chen',
    # 'Clinkz',
    'Clock',
    'CM',
    'DarkWillow',
    'Dazzle',
    'Disruptor',
    'Doom',
    # 'DP',
    'DragonKnight',
    'Drow',
    # 'DS',
    'EarthShaker',
    'EarthSpirit',
    'Elder',
    'EmberSpirit',
    'Enchantress',
    'Enigma',
    'Grandma',
    'Grim',
    'Gyro',
    'Huskar',
    'IceDuck',
    'Invoker',
    'IO',
    'Jakiro',
    'Juggernaut',
    'KOTL',
    'Kunkka',
    'LC',
    'LoneDruid',
    'Leshrac',
    'Lich',
    'Lina',
    'Lion',
    'Luna',
    'Lycan',
    # 'Magnus',
    'Mars',
    'Medusa',
    'Meepo',
    'Mirana',
    'MonkeyKing',
    'Morphling',
    # 'Naga',
    'Naix',
    'Necrophos',
    'Nevermore',
    'NP',
    # 'NS',
    'Nyx',
    'OD',
    'OgreMagi',
    'OmniKnight',
    'Oracle',
    'Panda',
    # 'Pangolier',
    # 'Phoenix',
    'PhuongAnh',
    # 'PhuongLinh',
    # 'Puck',
    'Pudge',
    # 'Pugna',
    'QOP',
    'Razor',
    # 'Riki',
    'Rubik',
    'SandKing',
    'SD',
    'ShadowShaman',
    # 'Silencer',
    # 'SkeletonKing',
    # 'SkywrathMage',
    'Sladar',
    'Slark',
    'Sniper',
    # 'Spectre',
    'Storm',
    'Sven',
    'TB',
    'Terrorist',
    'Tide',
    'Timber',
    'Tinker',
    'Tiny',
    'TramAnh',
    'Treant',
    'Troll',
    'Tuskar',
    # 'Underlord',
    # 'Undying',
    # 'Ursa',
    'Venom',
    'Viper',
    'Visage',
    'Void',
    # 'VoidSpirit',
    # 'VS',
    # 'Warlock',
    # 'Weaver',
    'WindRanger',
    'WitchDoctor',
    # 'WraithKing',
    'Zeus'
)

# classandspecies = ('Assassin', 'Aqir', 'DemonHunter', 'Druid', 'Hunter', 'Knight', 'Mage', 'Inventor', 'Priest', 'Shaman', 'Warlock', 'Warrior', 'Wizard', 'Dragon', 'Dwarf', 'Demon', 'Ogre', 'Elf', 'Undead', 'Orc', 'Goblin', 'Elemental', 'Razor', 'Enigma', 'Human', 'Naga', 'Troll', 'Beast', 'God', 'Kobold')

CAS_numbers = [int(file[:-4]) for file in os.listdir("C:/autochess_data/class_species_numbers/") if file.endswith("png")]
CAS_number_icons = [cv2.imread("C:/autochess_data/class_species_numbers/"+ file, 0) for file in os.listdir("C:/autochess_data/class_species_numbers/") if file.endswith("png")]
CAS_numbers_and_icons = tuple(zip(CAS_numbers, CAS_number_icons))

CAS_names = [file[:-4] for file in os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
CAS_icons = [cv2.imread("C:/autochess_data/class_species_icons/"+ file) for file in os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
CAS_names_and_icons = tuple(zip(CAS_names, CAS_icons))

CAS_dict = {'Aqir': [0, 0], 'Assassin': [0, 0], 'Beast': [0, 0], 'Tauren': [0, 0], 'Demon': [0, 0], 'Dragon': [0, 0], 'Druid': [0, 0], 'Dwarf': [0, 0], 'Elemental': [0, 0], 'Elf': [0, 0], 'Faceless': [0, 0], 'Goblin': [0, 0], 'God': [0, 0], 'Human': [0, 0], 'Hunter': [0, 0], 'Inventor': [0, 0], 'Knight': [0, 0], 'Kobold': [0, 0], 'Mage': [0, 0], 'Monk': [0, 0], 'Naga': [0, 0], 'Ogre': [0, 0], 'Orc': [0, 0], 'Pandaren': [0, 0], 'Priest': [0, 0], 'Shaman': [0, 0], 'Troll': [0, 0], 'Undead': [0, 0], 'Warlock': [0, 0], 'Warrior': [0, 0], 'Wizard': [0, 0]}

on_stage_CAS_x_coors = (1136,1327)
on_stage_CAS_y_coors = ((202, 289), (202, 373), (202, 460), (202, 547), (202, 635), (202, 723), (202, 810), (202, 897))



# creates Dictionary for Rank, Species, Class, and number of heroes left in Pool for creating table
RSCP_Dict = {}
RSCP_Dict = {

             'Barathum': ['1G', 'Tauren', 'Assassin', 'Barathum', 45],
             'Axe': ['1G', 'Orc', 'Warrior', 'Axe', 45],
             'Enchantress': ['1G', 'Beast', 'Druid', 'Enchantress', 45],
             'Tuskar': ['1G', 'Beast', 'Warrior', 'Tuskar', 45],
             'Drow': ['1G', 'Undead', 'Hunter', 'Drow', 45],
             'BH': ['1G', 'Goblin', 'Assassin', 'BH', 45],
             'Clock': ['1G', 'Goblin', 'Inventor', 'Clock', 45],
             'ShadowShaman': ['1G', 'Troll', 'Shaman', 'ShadowShaman', 45],
             'Tinker': ['1G', 'Goblin', 'Inventor', 'Tinker', 45],
             'AM': ['1G', 'Elf', 'DemonHunter', 'AM', 45],
             'Tiny': ['1G', 'Elemental', 'Warrior', 'Tiny', 45],
             'Mars': ['1G', 'God', 'Warrior', 'Mars', 45],
             'IceDuck': ['1G', 'Dragon', 'Mage', 'IceDuck', 45],
             'CM': ['1G', 'Human', 'Mage', 'CM', 45],
             'Luna': ['1G', 'Elf', 'Knight', 'Luna', 45],
             'WitchDoctor': ['1G', 'Troll', 'Warlock', 'WitchDoctor', 45],
             'Lion': ['2G', 'Demon', 'Wizard', 'Lion', 30],
             'Batrider': ['2G', 'Troll', 'Knight', 'Batrider', 30],
             'OgreMagi': ['2G', 'Ogre', 'Mage', 'OgreMagi', 30],
             'BeastMaster': ['2G', 'Orc', 'Hunter', 'BeastMaster', 30],
             'Juggernaut': ['2G', 'Orc', 'Warrior', 'Juggernaut', 30],
             'Timber': ['2G', 'Goblin', 'Inventor', 'Timber', 30],
             'Chaos': ['2G', 'Demon', 'Knight', 'Chaos', 30],
             'Morphling': ['2G', 'Elemental', 'Assassin', 'Morphling', 30],
             'NP': ['2G', 'Elf', 'Druid', 'NP', 30],
             'Mirana': ['2G', 'Elf', 'Hunter', 'Mirana', 30],
             'Slark': ['2G', 'Naga', 'Assassin', 'Slark', 30],
             'Dazzle': ['2G', 'Troll', 'Priest', 'Dazzle', 30],
             'Sniper': ['2G', 'Dwarf', 'Hunter', 'Sniper', 30],
             'Abaddon': ['2G', 'Undead', 'Knight', 'Abaddon', 30],
             'Oracle': ['2G', 'God', 'Priest', 'Oracle', 30],
             'Panda': ['2G', 'Pandaren', 'Monk', 'Panda', 30],
             'EmberSpirit': ['3G', 'Pandaren', 'Assassin', 'EmberSpirit', 30],
             'StormSpirit': ['3G', 'Pandaren', 'Mage', 'StormSpirit', 30],
             'EarthSpirit': ['3G', 'Pandaren', 'Shaman', 'EarthSpirit', 30],
             'Venom': ['3G', 'Aqir/Beast', 'Warlock', 'Venom', 25],
             'OmniKnight': ['3G', 'Human', 'Knight', 'OmniKnight', 25],
             'Razor': ['3G', 'Elemental', 'Mage', 'Razor', 25],
             'PhuongAnh': ['3G', 'Elf', 'Assassin', 'PhuongAnh', 25],
             'Treant': ['3G', 'Elf', 'Druid', 'Treant', 25],
             'Sladar': ['3G', 'Naga', 'Warrior', 'Sladar', 25],
             'SandKing': ['3G', 'Aqir', 'Assassin', 'SandKing', 25],
             'Lycan': ['3G', 'Human/Beast', 'Warrior', 'Lycan', 25],
             'TB': ['3G', 'Demon', 'DemonHunter', 'TB', 25],
             'Viper': ['3G', 'Dragon', 'Assassin', 'Viper', 25],
             'Nevermore': ['3G', 'Demon', 'Warlock', 'Nevermore', 25],
             'LC': ['3G', 'Human', 'Knight', 'LC', 25],
             'Lina': ['3G', 'Human', 'Mage', 'Lina', 25],
             'Visage': ['3G', 'Dragon/Undead', 'Hunter', 'Visage', 25],
             'Rubik': ['3G', 'God', 'Wizard', 'Rubik', 25],
             'Meepo': ['3G', 'Kobold', 'Inventor', 'Meepo', 25],
             'Void': ['3G', 'Faceless', 'Assassin', 'Void', 25],
             'WindRanger': ['4G', 'Elf', 'Hunter', 'WindRanger', 15],
             'Doom': ['4G', 'Demon', 'Warrior', 'Doom', 15],
             'Kunkka': ['4G', 'Human', 'Warrior', 'Kunkka', 15],
             'Grim': ['4G', 'Demon', 'Wizard', 'Grim', 15],
             'KOTL': ['4G', 'Human', 'Mage', 'KOTL', 15],
             'Necrophos': ['4G', 'Undead', 'Warlock', 'Necrophos', 15],
             'Alchemist': ['4G', 'Goblin', 'Warlock', 'Alchemist', 15],
             'DragonKnight': ['4G', 'Human/Dragon', 'Knight', 'DragonKnight', 15],
             'Medusa': ['4G', 'Naga', 'Hunter', 'Medusa', 15],
             'LoneDruid': ['4G', 'Beast', 'Druid', 'LoneDruid', 15],
             'Chen': ['4G', 'Orc', 'Priest', 'Chen', 15],
             'Nyx': ['4G', 'Aqir', 'Assassin', 'Nyx', 15],
             'Brood': ['4G', 'Aqir', 'Hunter', 'Brood', 15],
             'EarthShaker': ['4G', 'Chieftan', 'Shaman', 'EarthShaker', 15],
             'Disruptor': ['5G', 'Orc', 'Shaman', 'Disruptor', 10],
             'Gyro': ['5G', 'Dwarf', 'Inventor', 'Gyro', 10],
             'Tide': ['5G', 'Naga', 'Hunter', 'Tide', 10],
             'Enigma': ['5G', 'Elemental', 'Warlock', 'Enigma', 10],
             'Terrorist': ['5G', 'Goblin', 'Inventor', 'Terrorist', 10],
             'Elder': ['5G', 'God/Tauren', 'Druid', 'Elder', 10],
             'Sven': ['5G', 'Demon', 'Warrior', 'Sven', 10],
             'Zeus': ['5G', 'God', 'Mage', 'Zeus', 10],
             'QOP': ['5G', 'Demon', 'Assassin', 'QOP', 10],
             'TramAnh': ['5G', 'Elf', 'Assassin', 'TramAnh', 10],
             'MonkeyKing': ['5G', 'Beast', 'Monk', 'MonkeyKing', 10],
             'Invoker': ['5G', 'Elf', 'Mage', 'Invoker', 10],
             'Huskar': ['5G', 'Troll', 'Warrior', 'Huskar', 10],
             'Jakiro': ['5G', 'Dragon', 'Mage', 'Jakiro', 10],
             'Snapfire': ['5G', 'Goblin', 'Knight', 'Snapfire', 10],
             'IO': ['5G', 'Elf', 'Elf', 'IO', 10]

             }

# Loads all hero icons to memory
hero_icon_dict = {}
for hero in namelist:
    file_path = "C:/autochess_data/hero_icons/" + hero + ".png"
    hero_icon_dict[hero] = cv2.imread(file_path)

# Loads level icons to memory
level_dict = {}
level_dict[""] = cv2.imread("G:/level/1.png", 0)
level_dict["2"] = cv2.imread("G:/level/2.png", 0)
level_dict["3"] = cv2.imread("G:/level/3.png", 0)

TIMESLEEP = 0.6

HERO_ICON_WIDTH = 33
FIRST_X_START = 711
FIRST_X_END = 744

SECOND_X_START = FIRST_X_START + HERO_ICON_WIDTH
SECOND_X_END = FIRST_X_END + HERO_ICON_WIDTH

THIRD_X_START = SECOND_X_START + HERO_ICON_WIDTH + 1
THIRD_X_END = SECOND_X_END + HERO_ICON_WIDTH + 1

FOURTH_X_START = THIRD_X_START + HERO_ICON_WIDTH
FOURTH_X_END = THIRD_X_END + HERO_ICON_WIDTH

FIFTH_X_START = FOURTH_X_START + HERO_ICON_WIDTH
FIFTH_X_END = FOURTH_X_END + HERO_ICON_WIDTH

SIXTH_X_START = FIFTH_X_START + HERO_ICON_WIDTH + 1
SIXTH_X_END = FIFTH_X_END + HERO_ICON_WIDTH + 1

SEVENTH_X_START = SIXTH_X_START + HERO_ICON_WIDTH
SEVENTH_X_END = SIXTH_X_END + HERO_ICON_WIDTH

EIGHTH_X_START = SEVENTH_X_START + HERO_ICON_WIDTH
EIGHTH_X_END = SEVENTH_X_END + HERO_ICON_WIDTH

NINTH_X_START = EIGHTH_X_START + HERO_ICON_WIDTH + 1
NINTH_X_END = EIGHTH_X_END + HERO_ICON_WIDTH + 1

TENTH_X_START = NINTH_X_START + HERO_ICON_WIDTH
TENTH_X_END = NINTH_X_END + HERO_ICON_WIDTH

PLAYER_DISTANCE = 88
FIRST_Y_START = 221
FIRST_Y_END = 256

SECOND_Y_START = FIRST_Y_START + PLAYER_DISTANCE
SECOND_Y_END = FIRST_Y_END + PLAYER_DISTANCE

THIRD_Y_START = SECOND_Y_START + PLAYER_DISTANCE - 1
THIRD_Y_END = SECOND_Y_END + PLAYER_DISTANCE - 1

FOURTH_Y_START = THIRD_Y_START + PLAYER_DISTANCE - 1
FOURTH_Y_END = THIRD_Y_END + PLAYER_DISTANCE - 1

FIFTH_Y_START = FOURTH_Y_START + PLAYER_DISTANCE
FIFTH_Y_END = FOURTH_Y_END + PLAYER_DISTANCE

SIXTH_Y_START = FIFTH_Y_START + PLAYER_DISTANCE
SIXTH_Y_END = FIFTH_Y_END + PLAYER_DISTANCE

SEVENTH_Y_START = SIXTH_Y_START + PLAYER_DISTANCE - 1
SEVENTH_Y_END = SIXTH_Y_END + PLAYER_DISTANCE - 1

EIGHTH_Y_START = SEVENTH_Y_START + PLAYER_DISTANCE - 1
EIGHTH_Y_END = SEVENTH_Y_END + PLAYER_DISTANCE - 1

X_COORDINATES_START = (
FIRST_X_START, SECOND_X_START, THIRD_X_START, FOURTH_X_START, FIFTH_X_START, SIXTH_X_START, SEVENTH_X_START,
EIGHTH_X_START, NINTH_X_START, TENTH_X_START)
X_COORDINATES_END = (
FIRST_X_END, SECOND_X_END, THIRD_X_END, FOURTH_X_END, FIFTH_X_END, SIXTH_X_END, SEVENTH_X_END, EIGHTH_X_END,
NINTH_X_END, TENTH_X_END)
Y_COORDINATES_START = (
FIRST_Y_START, SECOND_Y_START, THIRD_Y_START, FOURTH_Y_START, FIFTH_Y_START, SIXTH_Y_START, SEVENTH_Y_START,
EIGHTH_Y_START)
Y_COORDINATES_END = (
FIRST_Y_END, SECOND_Y_END, THIRD_Y_END, FOURTH_Y_END, FIFTH_Y_END, SIXTH_Y_END, SEVENTH_Y_END, EIGHTH_Y_END)

LEVEL_ICON_HEIGHT = 7

LEVEL_AND_HERO_ICON_HEIGHT = 42

ICON_FIRST_ROI = (0, LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_SECOND_ROI = (LEVEL_AND_HERO_ICON_HEIGHT, 2 * LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_THIRD_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 2, 3 * LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_FOURTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 3, 4 * LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_FIFTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 4, 5 * LEVEL_AND_HERO_ICON_HEIGHT, 0, HERO_ICON_WIDTH)
ICON_SIXTH_ROI = (0, LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_SEVENTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT, 2 * LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_EIGHTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 2, 3 * LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_NINETH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 3, 4 * LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)
ICON_TENTH_ROI = (LEVEL_AND_HERO_ICON_HEIGHT * 4, 5 * LEVEL_AND_HERO_ICON_HEIGHT, 161, 161 + HERO_ICON_WIDTH)

ROI_TUPLE = (
ICON_FIRST_ROI, ICON_SECOND_ROI, ICON_THIRD_ROI, ICON_FOURTH_ROI, ICON_FIFTH_ROI, ICON_SIXTH_ROI, ICON_SEVENTH_ROI,
ICON_EIGHTH_ROI, ICON_NINETH_ROI, ICON_TENTH_ROI)

to_show_list = []
on_stage_list = []

"""
DEFINES FUNCTIONS FOR BUTTONS
"""


def thread(function, arg=None):
    if arg == None:
        x = threading.Thread(target=function)
        x.start()
    else:
        x = threading.Thread(target=function(arg))
        x.start()


# DEFINES WHAT SCAN BUTTON DOES
# def Scan():
#     try:
#         dota = gw.getWindowsWithTitle("Dota 2")[0]
#         dota.activate()
#     except IndexError as error:
#         pass
#     time.sleep(0.2)
#     pyautogui.click(x=347, y=798)
#     pyautogui.click(x=348, y=798)
#     pyautogui.click(x=349, y=798)
#
#
#     # window.progressbar.setText("Occupying mouse for taking pictures, please don't use it...")
#     # window.progressbar.setVisible(True)
#
#     os.chdir("C:/autochess_data")
#     screenshot = pyautogui.screenshot()
#     screenshot = np.asarray(screenshot)
#     player_status_list = [screenshot[438:449, 1705:1754], screenshot[525:536, 1705:1754], screenshot[613:624, 1705:1754], screenshot[701:712, 1705:1754], screenshot[788:799, 1705:1754],
#                           screenshot[875:886, 1705:1754]]
#
#     failed_icon = cv2.imread("C:/autochess_data/failed_icon.png")
#     transparent_failed_icon = cv2.imread("C:/autochess_data/transparent_failed_icon.png")
#
#     num_of_lost_players = 0
#     for i in range(0, len(player_status_list)):
#         if max(cv2.matchTemplate(player_status_list[i], failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8 or max(
#                 cv2.matchTemplate(player_status_list[i], transparent_failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8:
#             num_of_lost_players = 6 - i
#             break
#
#     keyboard.press_and_release("f3")
#     time.sleep(0.5)
#     on_stage_heroes = pyautogui.screenshot()
#     keyboard.press_and_release("f3")
#     on_stage_heroes.save("on_stage_heroes.png")
#     time.sleep(0.3)
#
#     count = 0
#     pyautogui.click(x=1602, y=233)
#     pyautogui.click(x=1602, y=233)
#     time.sleep(TIMESLEEP)
#     img = pyautogui.screenshot(region=(527, 619, 848, 212))
#     count += 1
#     img.save(f"{count}.jpg")
#
#     pyautogui.click(x=1602, y=320)
#     pyautogui.click(x=1602, y=320)
#     time.sleep(TIMESLEEP)
#     img = pyautogui.screenshot(region=(527, 619, 848, 212))
#     count += 1
#     img.save(f"{count}.jpg")
#
#     if num_of_lost_players < 6:
#         pyautogui.click(x=1602, y=409)
#         pyautogui.click(x=1602, y=409)
#         time.sleep(TIMESLEEP)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     if num_of_lost_players < 5:
#         pyautogui.click(x=1602, y=497)
#         pyautogui.click(x=1602, y=497)
#         time.sleep(TIMESLEEP)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     if num_of_lost_players < 4:
#         pyautogui.click(x=1602, y=586)
#         pyautogui.click(x=1602, y=586)
#         time.sleep(TIMESLEEP)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     if num_of_lost_players < 3:
#         pyautogui.click(x=1602, y=670)
#         pyautogui.click(x=1602, y=670)
#         pyautogui.moveTo(x=1546, y=620)
#         time.sleep(0.6)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     if num_of_lost_players < 2:
#         pyautogui.click(x=1602, y=758)
#         pyautogui.click(x=1602, y=758)
#         pyautogui.moveTo(x=1546, y=708)
#         time.sleep(0.6)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     if num_of_lost_players < 1:
#         pyautogui.click(x=1602, y=844)
#         pyautogui.click(x=1602, y=844)
#         pyautogui.moveTo(x=1546, y=794)
#         time.sleep(0.6)
#         img = pyautogui.screenshot(region=(527, 619, 848, 212))
#         count += 1
#         img.save(f"{count}.jpg")
#     else:
#         img = cv2.imread("C:/autochess_data/Lost.png")
#         count += 1
#         cv2.imwrite(f"{count}.jpg", img)
#
#     # window.progressbar.setText("Feeding pictures to the neural network...")
#
#     os.chdir("G:/darknet/")
#     os.system("G:\darknet/darknet.exe detector test G:\darknet/obj.data G:/darknet/thresh_cfg.cfg G:\darknetsave/yolov4-obj_last_25.weights -ext_output -dont_show -out result.json < data/train.txt")
#
#     f = open("G:/darknet/result.json")
#     data = json.load(f)
#
#     all_chess_pieces_list = ([], [], [], [], [], [], [], [])
#     for i in range(8):
#         for hero in data[i]["objects"]:
#             all_chess_pieces_list[i].append(hero["name"])
#
#     on_stage_heroes = cv2.imread("C:/autochess_data/on_stage_heroes.png")
#     on_stage_heroes_grayed = cv2.cvtColor(on_stage_heroes, cv2.COLOR_BGR2GRAY)
#     temp_on_stage_list = ([], [], [], [], [], [], [], [])
#     os.chdir("C:/autochess_data/")
#     count3 = 0
#     num_of_lost_players = 0
#
#     # window.progressbar.setText("Template matching icons...")
#
#     for i in range(0, 80 - num_of_lost_players * 10):
#         if i % 10 == 0:
#             count3 = 0 + int(i / 10)
#
#         hero_level = ""
#         level_icon_template = on_stage_heroes_grayed[
#                               Y_COORDINATES_END[count3] + 1:Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT,
#                               X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
#         for level in level_dict:
#             res = cv2.matchTemplate(level_dict[level], level_icon_template, cv2.TM_CCOEFF_NORMED)
#             if max(res) > 0.7:
#                 hero_level = level
#                 break
#
#         template = on_stage_heroes[Y_COORDINATES_START[count3]:Y_COORDINATES_END[count3],
#                    X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
#         all_matches = []
#         for hero_name in namelist:
#             cv2.waitKey(0)
#             res = cv2.matchTemplate(hero_icon_dict[hero_name], template, cv2.TM_CCOEFF_NORMED)
#             loc = np.where(res >= 0.65)
#             if loc[0].size > 0:
#                 all_matches.append((hero_name, max(res)))
#
#         all_matches = sorted(all_matches, key=lambda match: match[1])
#         if len(all_matches) > 0:
#             all_chess_pieces_list[count3].append(all_matches[-1][0] + hero_level)
#             temp_on_stage_list[count3].append((all_matches[-1][0] + hero_level, Y_COORDINATES_START[count3],
#                                                Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT,
#                                                X_COORDINATES_START[i % 10], X_COORDINATES_END[i % 10]))
#
#     # window.progressbar.setText("Tabulating the results...")
#
#     flat_list = [item for sublist in all_chess_pieces_list for item in sublist]
#
#     Dict = copy.deepcopy(RSCP_Dict)
#
#     for hero in flat_list:
#         if hero.endswith("2"):
#             Dict[hero[:-1]][4] -= 3
#         elif hero.endswith("3"):
#             Dict[hero[:-1]][4] -= 9
#         else:
#             Dict[hero][4] -= 1
#
#     colors = [Qt.white, QtGui.QColor(170, 170, 255), QtGui.QColor(90, 90, 255), QtGui.QColor(249, 28, 249),
#               QtGui.QColor(255, 151, 36)]
#     row = 0
#     for hero in Dict:
#         window.tableWidget.setItem(row, 4, QTableWidgetItem(str(Dict[hero][4])))
#         window.tableWidget.item(row, 4).setForeground(colors[int(Dict[hero][0][0]) - 1])
#         row += 1
#
#
#     CAS_dict_copy = copy.deepcopy(CAS_dict)
#
#     on_stage_CAS_icons = on_stage_heroes[
#                          on_stage_CAS_y_coors[7 - num_of_lost_players][0]:on_stage_CAS_y_coors[7 - num_of_lost_players][
#                              1],
#                          on_stage_CAS_x_coors[0]:on_stage_CAS_x_coors[1]]
#     on_stage_CAS_icons_grayed = cv2.cvtColor(on_stage_CAS_icons, cv2.COLOR_BGR2GRAY)
#
#     for CAS in CAS_names_and_icons:
#         result = cv2.matchTemplate(on_stage_CAS_icons, CAS[1], cv2.TM_CCOEFF_NORMED)
#         loc = np.where(result >= 0.9)
#         if loc[0].size == 0:
#             continue
#         else:
#             CAS_dict_copy[CAS[0]][0] = loc[0].size
#             for i in range(loc[0].size):
#                 number_icon = on_stage_CAS_icons_grayed[loc[0][i] + 25:loc[0][i] + 37, loc[1][i] + 2:loc[1][i] + 19]
#                 result_list = []
#                 for icon in CAS_numbers_and_icons:
#                     if cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED) > 0.85:
#                         result_list.append((icon[0], cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED)))
#                 result_list = sorted(result_list, key=lambda icon: icon[1], reverse=True)
#                 CAS_dict_copy[CAS[0]][1] += result_list[0][0]
#
#     row = 0
#     for CAS in CAS_dict_copy:
#         window.CAS_tableWidget.setItem(row, 0, QTableWidgetItem(CAS))
#         window.CAS_tableWidget.setItem(row, 1, QTableWidgetItem(str(CAS_dict_copy[CAS][0])))
#         window.CAS_tableWidget.setItem(row, 2, QTableWidgetItem(str(CAS_dict_copy[CAS][1])))
#         window.CAS_tableWidget.item(row, 0).setForeground(Qt.white)
#         window.CAS_tableWidget.item(row, 1).setTextAlignment(Qt.AlignHCenter)
#         window.CAS_tableWidget.item(row, 1).setForeground(Qt.white)
#         window.CAS_tableWidget.item(row, 2).setTextAlignment(Qt.AlignHCenter)
#         window.CAS_tableWidget.item(row, 2).setForeground(Qt.white)
#         row += 1
#
#
#
#     global to_show_list
#     to_show_list = all_chess_pieces_list
#     global on_stage_list
#     on_stage_list = temp_on_stage_list
#     print(temp_on_stage_list)


# DEFINES WHAT SHOW PREDICTIONS BUTTON DOES
def show_predictions():
    HEIGHT = 212
    WIDTH = 848
    COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255), (0, 0, 255), (255, 255, 255),
              (125, 0, 255), (255, 0, 125), (125, 255, 0), (0, 255, 125), (0, 125, 255), (255, 125, 0), (125, 75, 0),
              (0, 75, 125), (0, 125, 75), (75, 125, 0), (75, 0, 125), (125, 0, 75)]
    f = open("C:/autochess_data/result.json")
    data = json.load(f)
    global on_stage_list
    on_stage_img = cv2.imread("C:/autochess_data/on_stage_heroes.png")
    first_half = np.zeros((0, 1160, 3), dtype=np.uint8)
    second_half = np.zeros((0, 1160, 3), dtype=np.uint8)
    os.chdir("C:/autochess_data")
    for i in range(0, len(data)):
        img = cv2.imread(f"C:/autochess_data/{i + 1}.jpg")
        for hero in data[i]['objects']:
            x_start = round(
                hero["relative_coordinates"]["center_x"] * WIDTH - hero["relative_coordinates"]["width"] * WIDTH / 2)
            x_end = round(
                hero["relative_coordinates"]["center_x"] * WIDTH + hero["relative_coordinates"]["width"] * WIDTH / 2)
            y_start = round(
                hero["relative_coordinates"]["center_y"] * HEIGHT - hero["relative_coordinates"]["height"] * HEIGHT / 2)
            y_end = round(
                hero["relative_coordinates"]["center_y"] * HEIGHT + hero["relative_coordinates"]["height"] * HEIGHT / 2)
            cv2.rectangle(img, (x_start, y_start), (x_end, y_end), COLORS[int(hero['class_id']) % len(COLORS)], 1)
            cv2.putText(img, hero['name'], (x_start, y_start - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                        COLORS[int(hero['class_id']) % len(COLORS)], 1)
            cv2.putText(img, f"player{i + 1}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        count = 0
        bg = np.zeros((212, 312, 3), dtype=np.uint8)
        bg[0:210, :] = 255

        for hero in on_stage_list[i]:
            icon = on_stage_img[hero[1]:hero[2] - 1, hero[3]:hero[4]]
            bg[ROI_TUPLE[count][0]:ROI_TUPLE[count][1], ROI_TUPLE[count][2]:ROI_TUPLE[count][3]] = icon
            cv2.putText(bg, hero[0], (ROI_TUPLE[count][2] + HERO_ICON_WIDTH, ROI_TUPLE[count][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            count += 1
        img = cv2.hconcat([bg, img])

        if i in range(0, 4):
            first_half = cv2.vconcat([first_half, img])
        if i in range(4, 8):
            second_half = cv2.vconcat([second_half, img])

    all_predictions = cv2.hconcat([first_half, second_half])
    cv2.imwrite("C:/autochess_data/all_predictions.jpg", all_predictions)
    os.system("C:/autochess_data/all_predictions.jpg")


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPalette, QFont, QTextCursor
import sys
from string import ascii_lowercase

class TableSearch(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setEditTriggers(self.NoEditTriggers)
        self.searchWidget = QtWidgets.QLabel(self)
        self.searchWidget.setStyleSheet('''
            QLabel {
                border: 0px inset darkGray; 
                border-radius: 0px;
                background-color: rgba(12, 12, 12, 10);
                font-size: 36px;
                height: 48px;
                width: 120px;
                color: Gray
            }
            ''')
        self.searchWidget.hide()
        self.searchTimer = QtCore.QTimer(
            singleShot=True,
            timeout=self.resetSearch,
            interval=QtWidgets.QApplication.instance().keyboardInputInterval())

        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setShowGrid(False)
        self.horizontalHeader().setMinimumSectionSize(0)
        self.setFrameStyle(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setMinimumSectionSize(0)
        self.verticalHeader().setDefaultSectionSize(30)



    def resetSearch(self):
        self.searchWidget.setText('')
        self.searchWidget.hide()

    def updateSearchWidget(self):
        if not self.searchWidget.text():
            self.searchWidget.hide()
            return
        self.searchWidget.show()
        self.searchWidget.adjustSize()
        geo = self.searchWidget.geometry()
        geo.moveBottomRight(
            self.viewport().geometry().bottomRight() - QtCore.QPoint(200, 200))
        self.searchWidget.setGeometry(geo)

    def keyboardSearch(self, search):
        super().keyboardSearch(search)
        if not search:
            self.searchWidget.setText('')
        else:
            text = self.searchWidget.text()
            if not text:
                text = ''
            text += search
            self.searchWidget.setText(text)
        self.updateSearchWidget()
        self.searchTimer.start()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateSearchWidget()

class Strategies(QWidget):
    def __init__(self):
        super().__init__()
        self.UiC()

    def UiC(self):
        self.layout = QGridLayout()
        self.setWindowTitle("Strategies and Tips")
        self.setGeometry(520, 120, 500, 500)
        self.completer = QCompleter(namelist + tuple(CAS_names))
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

        self.SearchWidget = QLineEdit()
        self.SearchWidget.setCompleter(self.completer)

        self.TextBody = QTextEdit()
        text = open('C:/autochess_data/Strategies.txt').read()
        self.TextBody.setMarkdown(text)
        self.TextBody.setReadOnly(True)
        self.TextBody.installEventFilter(self)

        self.EditButton = QPushButton("Edit")
        self.EditButton.clicked.connect(self.edit)

        self.SearchButton = QPushButton("Search")
        self.SearchButton.clicked.connect(self.find)

        self.SaveButton = QPushButton("Save to Github")
        self.SaveButton.clicked.connect(self.save_to_github)

        self.layout.addWidget(self.SearchWidget, 0, 0, 1, 3)
        self.layout.addWidget(self.SearchButton, 0, 3, 1, 1)
        self.layout.addWidget(self.TextBody, 1, 0, 1, 4)
        self.layout.addWidget(self.EditButton, 2, 0, 1, 2)
        self.layout.addWidget(self.SaveButton, 2, 2, 1, 2)
        self.setLayout(self.layout)

    def find(self):
        text = "(cat) " + self.SearchWidget.text()
        self.TextBody.setFocus()
        self.TextBody.moveCursor(QTextCursor.End)
        self.TextBody.find(text, QtGui.QTextDocument.FindBackward)

    def edit(self):
        self.TextBody.setReadOnly(False)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusOut and
                source is self.TextBody):
            self.TextBody.setReadOnly(True)
            text = self.TextBody.toMarkdown()
            with open("C:/autochess_data/Strategies.txt", "w") as f:
                f.write(text)
        return super(Strategies, self).eventFilter(source, event)

    def save_to_github(self):

        with open("C:/autochess_data/Strategies.txt", "w") as f:
            f.write(self.TextBody.toMarkdown())
        path = "https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt"


        r = requests.get(path, auth=(user, token))
        if not r.ok:
            print("Error when retrieving branch info from %s" % path)
            print("Reason: %s [%d]" % (r.text, r.status_code))

        sha = r.json()['sha']

        content = ""

        with open("C:/autochess_data/Strategies.txt", "r") as data:
            data = data.read().encode("utf-8")
            data = base64.b64encode(data)
            content = data.decode("utf-8")

        inputdata = {}
        inputdata["path"] = path
        inputdata["branch"] = "main"
        inputdata["message"] = "abc"
        inputdata["content"] = content
        inputdata["sha"] = sha

        try:
            rPut = requests.put(path, auth=(user, token), data=json.dumps(inputdata))
            if not rPut.ok:
                print("Error when pushing to %s")
                print("Reason: %s [%d]" % (rPut.text, rPut.status_code))
                raise Exception
        except requests.exceptions.RequestException as e:
            print(rPut)
            print(rPut.headers)
            print(rPut.text)

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.UiC()

    def UiC(self):
        self.scan_button = QPushButton("Scan", self)
        self.scan_button.clicked.connect(self.Scan)
        self.scan_button.setFixedSize(300,80)
        self.scan_button.move(69,730)
        # self.scan_button.clicked.connect(lambda state, x=self.Scan: thread(self.Scan))

        self.show_predict_button = QPushButton("Show Predictions", self)
        self.show_predict_button.clicked.connect(show_predictions)
        self.show_predict_button.setFixedSize(211, 70)
        self.show_predict_button.move(15, 820)
        self.show_predict_button.clicked.connect(lambda state, x=show_predictions: thread(show_predictions))


        self.show_strat_button = QPushButton("Strategies and Tips", self)
        self.show_strat_button.clicked.connect(self.show_strat)
        self.show_strat_button.setFixedSize(210, 70)
        self.show_strat_button.move(15, 900)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.Strategies = Strategies()

        self.CAS_tableWidget = TableSearch()
        self.CAS_tableWidget.setParent(self)
        self.CAS_tableWidget.setRowCount(len(CAS_dict))
        self.CAS_tableWidget.setColumnCount(3)
        self.CAS_tableWidget.setHorizontalHeaderLabels(["Class/Species", "players", "chesspieces"])
        self.CAS_tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.CAS_tableWidget.setColumnWidth(0, 90)
        self.CAS_tableWidget.setColumnWidth(1, 60)
        self.CAS_tableWidget.setColumnWidth(2, 90)
        self.CAS_tableWidget.setMaximumWidth(327)
        self.CAS_tableWidget.viewport().installEventFilter(self)
        self.CAS_tableWidget.doubleClicked.connect(self.onTableClicked)
        p = self.CAS_tableWidget.palette()
        p.setColor(QPalette.Base, QtGui.QColor(12, 12, 12))
        self.CAS_tableWidget.setPalette(p)
        self.CAS_tableWidget.horizontalHeader().setFont(font)
        self.CAS_tableWidget.setFont(font)
        self.CAS_tableWidget.move(102,0)

        row = 0
        for CAS in CAS_dict:
            self.CAS_tableWidget.setItem(row, 0, QTableWidgetItem(CAS))
            item1 = QTableWidgetItem()
            item1.setData(Qt.EditRole, QVariant(CAS_dict[CAS][0]))
            self.CAS_tableWidget.setItem(row, 1, item1)
            item2 = QTableWidgetItem()
            item2.setData(Qt.EditRole, QVariant(CAS_dict[CAS][1]))
            self.CAS_tableWidget.setItem(row, 2, item2)
            self.CAS_tableWidget.item(row, 0).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 1).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 1).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 2).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 2).setForeground(Qt.white)
            row +=1

        self.tableWidget = TableSearch()
        self.tableWidget.setParent(self)
        self.tableWidget.setRowCount(len(RSCP_Dict))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["R", "Species", "Class", "Name", "NO"])
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.tableWidget.setColumnWidth(0, 26)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 30)
        self.tableWidget.move(15, 200)
        self.tableWidget.resize(422,500)

        p = self.tableWidget.palette()
        p.setColor(QPalette.Base, QtGui.QColor(12, 12, 12))
        self.tableWidget.setPalette(p)
        self.tableWidget.viewport().installEventFilter(self)
        font.setPointSize(11)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.setFont(font)
        colors = [Qt.white, QtGui.QColor(170, 170, 255), QtGui.QColor(90, 90, 255), QtGui.QColor(249, 28, 249),
                  QtGui.QColor(255, 151, 36)]

        row = 0
        for hero in RSCP_Dict:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(RSCP_Dict[hero][0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(RSCP_Dict[hero][1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(RSCP_Dict[hero][2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(RSCP_Dict[hero][3]))
            item4 = QTableWidgetItem()
            item4.setData(Qt.EditRole, QVariant(RSCP_Dict[hero][4]))
            self.tableWidget.setItem(row, 4, item4)
            self.tableWidget.item(row, 0).setForeground(colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 1).setForeground(colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 2).setForeground(colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 3).setForeground(colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 4).setForeground(colors[int(RSCP_Dict[hero][0][0]) - 1])
            row += 1

        self.tableWidget.doubleClicked.connect(self.onTableClicked)

        self.progressbar = QProgressBar()
        self.progressbar.setRange(0, 0)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setFixedSize(700, 500)
        self.progressbar.move(800, 20)

        self.label = QLabel(self)
        self.label.setText("Mouse interval length (second):")
        self.label.move(250,890)

        self.label2 = QLabel(self)
        self.label2.setText("Set time intervals between camera flips.\nRecomendations: - 0.6 with dynamic fog\n                             -0.3 without")
        self.label2.move(240,905)

        self.editbox = QLineEdit(self)
        self.editbox.setFixedSize(25, 25)
        self.editbox.setPlaceholderText("0.6")
        self.editbox.installEventFilter(self)
        self.editbox.move(405,879)

        self.setWindowTitle("Autochess Probability Tracker")
        self.setFixedSize(450, 980)
        self.setGeometry(1, 24, 450, 980)


    def show_strat(self):
        self.Strategies.show()
        return

    def onTableClicked(self, index):
        if index.data().startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            return
        data = "(cat) " + index.data()
        print(data)
        self.Strategies.show()
        self.Strategies.TextBody.setFocus()
        self.Strategies.TextBody.moveCursor(QTextCursor.End)
        self.Strategies.TextBody.find(data, QtGui.QTextDocument.FindBackward)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusOut and
                source is self.editbox):
            global TIMESLEEP
            TIMESLEEP = float(self.editbox.text())
            print(TIMESLEEP, type(TIMESLEEP))
        return super(Myapp, self).eventFilter(source, event)

    def Scan(self):
        try:
            dota = gw.getWindowsWithTitle("Dota 2")[0]
            dota.activate()
        except IndexError as error:
            return
        time.sleep(0.2)
        pyautogui.click(x=347, y=798)
        pyautogui.click(x=348, y=798)
        pyautogui.click(x=349, y=798)

        # self.progressbar.("Occupying mouse for taking pictures, please don't use it...")
        self.progressbar.setVisible(True)
        # App.processEvents()




        os.chdir("C:/autochess_data")
        screenshot = pyautogui.screenshot()
        screenshot = np.asarray(screenshot)
        player_status_list = [screenshot[438:449, 1705:1754], screenshot[525:536, 1705:1754],
                              screenshot[613:624, 1705:1754], screenshot[701:712, 1705:1754],
                              screenshot[788:799, 1705:1754],
                              screenshot[875:886, 1705:1754]]

        failed_icon = cv2.imread("C:/autochess_data/failed_icon.png")
        transparent_failed_icon = cv2.imread("C:/autochess_data/transparent_failed_icon.png")

        num_of_lost_players = 0
        for i in range(0, len(player_status_list)):
            if max(cv2.matchTemplate(player_status_list[i], failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8 or max(
                    cv2.matchTemplate(player_status_list[i], transparent_failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8:
                num_of_lost_players = 6 - i
                break

        keyboard.press_and_release("f3")
        time.sleep(0.5)
        on_stage_heroes = pyautogui.screenshot()
        keyboard.press_and_release("f3")
        on_stage_heroes.save("on_stage_heroes.png")
        time.sleep(0.3)

        count = 0
        pyautogui.click(x=1602, y=233)
        pyautogui.click(x=1602, y=233)
        time.sleep(TIMESLEEP)
        img = pyautogui.screenshot(region=(527, 619, 848, 212))
        count += 1
        img.save(f"{count}.jpg")

        pyautogui.click(x=1602, y=320)
        pyautogui.click(x=1602, y=320)
        time.sleep(TIMESLEEP)
        img = pyautogui.screenshot(region=(527, 619, 848, 212))
        count += 1
        img.save(f"{count}.jpg")

        if num_of_lost_players < 6:
            pyautogui.click(x=1602, y=409)
            pyautogui.click(x=1602, y=409)
            time.sleep(TIMESLEEP)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 5:
            pyautogui.click(x=1602, y=497)
            pyautogui.click(x=1602, y=497)
            time.sleep(TIMESLEEP)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 4:
            pyautogui.click(x=1602, y=586)
            pyautogui.click(x=1602, y=586)
            time.sleep(TIMESLEEP)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 3:
            pyautogui.click(x=1602, y=670)
            pyautogui.click(x=1602, y=670)
            pyautogui.moveTo(x=1546, y=620)
            time.sleep(0.6)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 2:
            pyautogui.click(x=1602, y=758)
            pyautogui.click(x=1602, y=758)
            pyautogui.moveTo(x=1546, y=708)
            time.sleep(0.6)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 1:
            pyautogui.click(x=1602, y=844)
            pyautogui.click(x=1602, y=844)
            pyautogui.moveTo(x=1546, y=794)
            time.sleep(0.6)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.png")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        # self.progressbar.setText("Feeding pictures to the neural network...")
        # App.processEvents()

        os.chdir("G:/darknet/")
        os.system(
            "G:\darknet/darknet.exe detector test G:\darknet/obj.data G:/darknet/thresh_cfg.cfg G:\darknetsave/yolov4-obj_last_25.weights -ext_output -dont_show -out result.json < data/train.txt")

        f = open("G:/darknet/result.json")
        data = json.load(f)

        all_chess_pieces_list = ([], [], [], [], [], [], [], [])
        for i in range(8):
            for hero in data[i]["objects"]:
                all_chess_pieces_list[i].append(hero["name"])

        on_stage_heroes = cv2.imread("C:/autochess_data/on_stage_heroes.png")
        on_stage_heroes_grayed = cv2.cvtColor(on_stage_heroes, cv2.COLOR_BGR2GRAY)
        temp_on_stage_list = ([], [], [], [], [], [], [], [])
        os.chdir("C:/autochess_data/")
        count3 = 0
        num_of_lost_players = 0

        # self.progressbar.setText("Template matching icons...")
        # App.processEvents()

        for i in range(0, 80 - num_of_lost_players * 10):
            if i % 10 == 0:
                count3 = 0 + int(i / 10)

            hero_level = ""
            level_icon_template = on_stage_heroes_grayed[
                                  Y_COORDINATES_END[count3] + 1:Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT,
                                  X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
            for level in level_dict:
                res = cv2.matchTemplate(level_dict[level], level_icon_template, cv2.TM_CCOEFF_NORMED)
                if max(res) > 0.7:
                    hero_level = level
                    break

            template = on_stage_heroes[Y_COORDINATES_START[count3]:Y_COORDINATES_END[count3],
                       X_COORDINATES_START[i % 10]:X_COORDINATES_END[i % 10]]
            all_matches = []
            for hero_name in namelist:
                cv2.waitKey(0)
                res = cv2.matchTemplate(hero_icon_dict[hero_name], template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= 0.65)
                if loc[0].size > 0:
                    all_matches.append((hero_name, max(res)))

            all_matches = sorted(all_matches, key=lambda match: match[1])
            if len(all_matches) > 0:
                all_chess_pieces_list[count3].append(all_matches[-1][0] + hero_level)
                temp_on_stage_list[count3].append((all_matches[-1][0] + hero_level, Y_COORDINATES_START[count3],
                                                   Y_COORDINATES_END[count3] + 1 + LEVEL_ICON_HEIGHT,
                                                   X_COORDINATES_START[i % 10], X_COORDINATES_END[i % 10]))

        # self.progressbar.setText("Tabulating the results...")
        # App.processEvents()

        flat_list = [item for sublist in all_chess_pieces_list for item in sublist]

        Dict = copy.deepcopy(RSCP_Dict)

        for hero in flat_list:
            if hero.endswith("2"):
                Dict[hero[:-1]][4] -= 3
            elif hero.endswith("3"):
                Dict[hero[:-1]][4] -= 9
            else:
                Dict[hero][4] -= 1

        colors = [Qt.white, QtGui.QColor(170, 170, 255), QtGui.QColor(90, 90, 255), QtGui.QColor(249, 28, 249),
                  QtGui.QColor(255, 151, 36)]
        row = 0
        for hero in Dict:
            item4 = QTableWidgetItem()
            item4.setData(Qt.EditRole, QVariant(RSCP_Dict[hero][4]))
            self.tableWidget.setItem(row, 4, item4)
            self.tableWidget.item(row, 4).setForeground(colors[int(Dict[hero][0][0]) - 1])
            row += 1

        CAS_dict_copy = copy.deepcopy(CAS_dict)

        on_stage_CAS_icons = on_stage_heroes[
                             on_stage_CAS_y_coors[7 - num_of_lost_players][0]:
                             on_stage_CAS_y_coors[7 - num_of_lost_players][
                                 1],
                             on_stage_CAS_x_coors[0]:on_stage_CAS_x_coors[1]]
        on_stage_CAS_icons_grayed = cv2.cvtColor(on_stage_CAS_icons, cv2.COLOR_BGR2GRAY)

        for CAS in CAS_names_and_icons:
            result = cv2.matchTemplate(on_stage_CAS_icons, CAS[1], cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= 0.9)
            if loc[0].size == 0:
                continue
            else:
                CAS_dict_copy[CAS[0]][0] = loc[0].size
                for i in range(loc[0].size):
                    number_icon = on_stage_CAS_icons_grayed[loc[0][i] + 25:loc[0][i] + 37, loc[1][i] + 2:loc[1][i] + 19]
                    result_list = []
                    for icon in CAS_numbers_and_icons:
                        if cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED) > 0.85:
                            result_list.append((icon[0], cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED)))
                    result_list = sorted(result_list, key=lambda icon: icon[1], reverse=True)
                    CAS_dict_copy[CAS[0]][1] += result_list[0][0]

        row = 0
        for CAS in CAS_dict_copy:
            self.CAS_tableWidget.setItem(row, 0, QTableWidgetItem(CAS))
            item1 = QTableWidgetItem()
            item1.setData(Qt.EditRole, QVariant(CAS_dict_copy[CAS][0]))
            self.CAS_tableWidget.setItem(row, 1, item1)
            item2 = QTableWidgetItem()
            item2.setData(Qt.EditRole, QVariant(CAS_dict_copy[CAS][1]))
            self.CAS_tableWidget.setItem(row, 2, item2)
            print(CAS, CAS_dict[CAS][0], CAS_dict[CAS][1])
            self.CAS_tableWidget.item(row, 0).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 1).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 1).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 2).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 2).setForeground(Qt.white)
            row +=1

        global to_show_list
        to_show_list = all_chess_pieces_list
        global on_stage_list
        on_stage_list = temp_on_stage_list
        print(temp_on_stage_list)



App = QApplication(sys.argv)


window = Myapp()
window.show()


sys.exit(App.exec())
