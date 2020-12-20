import json
import os
import pyautogui
import time
import cv2
import numpy as np
from keyboard import press_and_release
from pygetwindow import getWindowsWithTitle
import sys
import copy
import requests
import base64
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QApplication, QSizePolicy, QTableWidget, QWidget, QProgressBar, QPushButton, QLineEdit, QCompleter, QTextEdit, QGridLayout,QFrame, QHeaderView, QLabel
from PyQt5.QtGui import QColor, QPalette, QFont, QTextCursor, QTextDocument
from string import ascii_lowercase
from PyQt5.QtCore import QThread, pyqtSignal, QVariant, Qt, QEvent, QTimer, QPoint

"""
LOADS DATA AND CONSTANTS TO RAM
"""
# Pulls Strategies.txt from Github repo
rGet = requests.get("https://api.github.com/repos/Michael-Evergreen/auto_chess/contents/Strategies.txt")
data = (base64.b64decode(rGet.json()['content']).decode("utf-8"))
with open("C:/autochess_data/Strategies.txt", "w") as f:
    f.write(data)

# Creates a folder to store data
try:
    os.mkdir("C:/autochess_data/")
except OSError as error:
    pass

# Tuple of all characters' names in correct order for mapping later
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
    'Spider',
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
    # 'Leshrac',
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
    # 'Naix',
    'Necrophos',
    'Nevermore',
    'NP',
    # 'NS',
    'Nyx',
    # 'OD',
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

# Create a tuple grouping different numbers and their corresponding icons
CAS_numbers = [int(file[:-4]) for file in os.listdir("C:/autochess_data/class_species_numbers/") if
               file.endswith("png")]
CAS_number_icons = [cv2.imread("C:/autochess_data/class_species_numbers/" + file, 0) for file in
                    os.listdir("C:/autochess_data/class_species_numbers/") if file.endswith("png")]
CAS_numbers_and_icons = tuple(zip(CAS_numbers, CAS_number_icons))

# Create a tuple grouping different classes/species and their corresponding icons
CAS_names = [file[:-4] for file in os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
CAS_icons = [cv2.imread("C:/autochess_data/class_species_icons/" + file) for file in
             os.listdir("C:/autochess_data/class_species_icons/") if file.endswith("png")]
CAS_names_and_icons = tuple(zip(CAS_names, CAS_icons))

# Creates a dict tracking classes'/species' popularity: how many players are using them, how many of them are being used.
# A table will be created later using this data
CAS_dict = {'Aqir': [0, 0], 'Assassin': [0, 0], 'Beast': [0, 0], 'Tauren': [0, 0], 'Demon': [0, 0], 'Dragon': [0, 0],
            'Druid': [0, 0], 'Dwarf': [0, 0], 'Elemental': [0, 0], 'Elf': [0, 0], 'Faceless': [0, 0], 'Goblin': [0, 0],
            'God': [0, 0], 'Human': [0, 0], 'Hunter': [0, 0], 'Inventor': [0, 0], 'Knight': [0, 0], 'Kobold': [0, 0],
            'Mage': [0, 0], 'Monk': [0, 0], 'Naga': [0, 0], 'Ogre': [0, 0], 'Orc': [0, 0], 'Pandaren': [0, 0],
            'Priest': [0, 0], 'Shaman': [0, 0], 'Troll': [0, 0], 'Undead': [0, 0], 'Warlock': [0, 0], 'Warrior': [0, 0],
            'Wizard': [0, 0]}

# Coordinates of class and species icons
on_stage_CAS_x_coors = (1136, 1327)
on_stage_CAS_y_coors = ((202, 289), (202, 373), (202, 460), (202, 547), (202, 635), (202, 723), (202, 810), (202, 897))

# Creates dict tracking Rank, Species, Class, and number of characters left in Pool.
# A table will be created later using this data.
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
    'DarkWillow': ['1G', 'Elf', 'Wizard', 'DarkWillow', 45],
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
    'Storm': ['3G', 'Pandaren', 'Mage', 'Storm', 30],
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
    'Spider': ['4G', 'Aqir', 'Hunter', 'Spider', 15],
    'EarthShaker': ['4G', 'Tauren', 'Shaman', 'EarthShaker', 15],
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
    'Grandma': ['5G', 'Goblin', 'Knight', 'Grandma', 10],
    'IO': ['5G', 'Elf', 'Elf', 'IO', 10]

}

# Loads all characters icons to memory
hero_icon_dict = {}
for hero in namelist:
    file_path = "C:/autochess_data/hero_icons/" + hero + ".png"
    hero_icon_dict[hero] = cv2.imread(file_path)

# Loads level icons to memory
level_dict = {}
level_dict[""] = cv2.imread("G:/level/1.png", 0)
level_dict["2"] = cv2.imread("G:/level/2.png", 0)
level_dict["3"] = cv2.imread("G:/level/3.png", 0)

# A global variable storing sleeping time between camera flicks
timesleep = 0.6

# Constant variables storing heights, widths, distances, coordinates, and regions of image where characters and their
# level icons are shown.
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

# Global variables storing list of all detected
to_show_list = []
on_stage_list = []


""" 
Creates a table class inheriting from QTableWidget that provides a visual aid for searching
"""
class TableSearch(QTableWidget):
    def __init__(self):
        super().__init__()

        # Styling
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setShowGrid(False)
        self.horizontalHeader().setMinimumSectionSize(0)
        self.setFrameStyle(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setMinimumSectionSize(0)
        self.verticalHeader().setDefaultSectionSize(30)

        # Disables editing on table's cell
        self.setEditTriggers(self.NoEditTriggers)

        # Creates a QLabel that acts as a visual aid
        self.visual_aid = QLabel(self)
        self.visual_aid.hide()

        # Styling
        self.visual_aid.setStyleSheet('''
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


        # Creates a QTimer that starts counting whenever a key is entered
        self.timer = QTimer(
            singleShot=True,
            timeout=self.reset_search,
            interval=QApplication.instance().keyboardInputInterval())

    # Defines a function that resets and hides QLabel's text when timeout
    def reset_search(self):
        self.visual_aid.setText('')
        self.visual_aid.hide()

    # Updates QLabel, adjust its style and position
    def update_visual_aid(self):
        if not self.visual_aid.text():
            self.visual_aid.hide()
            return
        self.visual_aid.show()
        self.visual_aid.adjustSize()
        geo = self.visual_aid.geometry()
        geo.moveBottomRight(
            self.viewport().geometry().bottomRight() - QPoint(200, 200))
        self.visual_aid.setGeometry(geo)

    # Overrides keyboardSearch to add text to QLabel and start timer
    def keyboardSearch(self, string):
        super().keyboardSearch(string)
        if not string:
            self.visual_aid.setText('')
        else:
            text = self.visual_aid.text()
            if not text:
                text = ''
            text += string
            self.visual_aid.setText(text)
        self.update_visual_aid()
        self.timer.start()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_visual_aid()


"""
Creates a window inheriting from QWidget to display Tips and Strategies
"""
class Strategies(QWidget):
    def __init__(self):
        super().__init__()

       # Creates a search box with auto suggestion
        self.search_widget = QLineEdit()
        self.completer = QCompleter(namelist + tuple(CAS_names))
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.search_widget.setCompleter(self.completer)

        # Creates a text body with data pulled from Github
        self.TextBody = QTextEdit()
        self.text = open('C:/autochess_data/Strategies.txt').read()
        self.TextBody.setMarkdown(self.text)
        self.TextBody.setReadOnly(True)
        self.TextBody.installEventFilter(self)

        # Creates a button that enables editing
        self.EditButton = QPushButton("Edit")
        self.EditButton.clicked.connect(self.edit)

        # Creates a button for searching
        self.SearchButton = QPushButton("Search")
        self.SearchButton.clicked.connect(self.find)

        # Creates a button for saving edited data to Github
        self.SaveButton = QPushButton("Save to Github")
        self.SaveButton.clicked.connect(self.save_to_github)

        # Creates a layout and positions widgets
        self.layout = QGridLayout()
        self.setWindowTitle("Strategies and Tips")
        self.setGeometry(520, 120, 500, 500)
        self.layout.addWidget(self.search_widget, 0, 0, 1, 3)
        self.layout.addWidget(self.SearchButton, 0, 3, 1, 1)
        self.layout.addWidget(self.TextBody, 1, 0, 1, 4)
        self.layout.addWidget(self.EditButton, 2, 0, 1, 2)
        self.layout.addWidget(self.SaveButton, 2, 2, 1, 2)
        self.setLayout(self.layout)

    # Defines a search function that searches backward to better show the results
    def find(self):
        self.text = "(cat) " + self.search_widget.text()
        self.TextBody.setFocus()
        self.TextBody.moveCursor(QTextCursor.End)
        self.TextBody.find(self.text, QTextDocument.FindBackward)

    # Enables edit when its corresponding button is clicked
    def edit(self):
        self.TextBody.setReadOnly(False)

    # Defines an event filter function that catches FocusOut signal from text body to save changes
    def eventFilter(self, source, event):
        if (event.type() == QEvent.FocusOut and
                source is self.TextBody):
            self.TextBody.setReadOnly(True)
            self.text = self.TextBody.toMarkdown()
            with open("C:/autochess_data/Strategies.txt", "w") as f:
                f.write(self.text)
        return super(Strategies, self).eventFilter(source, event)

    # Uses Github API to save changes when its button is clicked
    def save_to_github(self):
        user = "Michael-Evergreen"
        token = "10c025f6982de29bae3d60e51760f0863a79bb78"
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


"""
Creates a progress bar class inheriting from QProgressBar that allows setting text
"""
class MyProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar")
        self.setFont(QFont('Times', 20))
        self.setRange(0, 0)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setAlignment(Qt.AlignCenter)
        self._text = None

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text


"""
Creates the main GUI class inheriting from QWidget
"""
class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.UiC()

    def UiC(self):
        # Creates and positions Scan button, Show Predictions button, and Strategies and Tips button.
        # Connects their signal to appropriate slots.
        self.scan_button = QPushButton("Scan", self)
        self.scan_button.clicked.connect(self.Scan)
        self.scan_button.setFixedSize(300, 80)
        self.scan_button.move(69, 730)

        self.show_predict_button = QPushButton("Show Predictions", self)
        self.show_predict_button.clicked.connect(self.show_predictions)
        self.show_predict_button.setFixedSize(211, 70)
        self.show_predict_button.move(15, 820)

        self.show_strat_button = QPushButton("Strategies and Tips", self)
        self.show_strat_button.clicked.connect(self.show_strat)
        self.show_strat_button.setFixedSize(210, 70)
        self.show_strat_button.move(15, 900)

        self.Strategies = Strategies()

        # Defines some colors and fonts to be used later
        self.colors = [Qt.white, QColor(170, 170, 255), QColor(90, 90, 255), QColor(249, 28, 249),
                  QColor(255, 151, 36)]
        self.font = QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)


        """
        Creates the class' and species' popularity table
        """
        self.CAS_tableWidget = TableSearch()

        # Sets its parent to be this main GUI or it won't show up
        self.CAS_tableWidget.setParent(self)

        # Installs event filter and connect its clicked signal to the appropriate slot
        self.CAS_tableWidget.viewport().installEventFilter(self)
        self.CAS_tableWidget.doubleClicked.connect(self.onTableClicked)

        # Sets its rows' and columns' values
        self.CAS_tableWidget.setRowCount(len(CAS_dict))
        self.CAS_tableWidget.setColumnCount(3)
        self.CAS_tableWidget.setHorizontalHeaderLabels(["Class/Species", "players", "chesspieces"])
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
            row += 1

        # Styling and positioning
        self.CAS_tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.CAS_tableWidget.setColumnWidth(0, 90)
        self.CAS_tableWidget.setColumnWidth(1, 60)
        self.CAS_tableWidget.setColumnWidth(2, 90)
        self.CAS_tableWidget.setMaximumWidth(327)
        p = self.CAS_tableWidget.palette()
        p.setColor(QPalette.Base, QColor(12, 12, 12))
        self.CAS_tableWidget.setPalette(p)
        self.CAS_tableWidget.horizontalHeader().setFont(self.font)
        self.CAS_tableWidget.setFont(self.font)
        self.CAS_tableWidget.move(102, 0)

        """
        Creates the chess pieces table
        """
        self.tableWidget = TableSearch()

        # Sets its parent to be this main GUI or it won't show up
        self.tableWidget.setParent(self)

        # Installs event filter and connect its clicked signal to the appropriate slot
        self.tableWidget.viewport().installEventFilter(self)
        self.tableWidget.doubleClicked.connect(self.onTableClicked)

        # Sets its rows' and columns' values
        self.tableWidget.setRowCount(len(RSCP_Dict))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["R", "Species", "Class", "Name", "NO"])
        row = 0
        for hero in RSCP_Dict:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(RSCP_Dict[hero][0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(RSCP_Dict[hero][1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(RSCP_Dict[hero][2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(RSCP_Dict[hero][3]))
            item4 = QTableWidgetItem()
            item4.setData(Qt.EditRole, QVariant(RSCP_Dict[hero][4]))
            self.tableWidget.setItem(row, 4, item4)
            self.tableWidget.item(row, 0).setForeground(self.colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 1).setForeground(self.colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 2).setForeground(self.colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 3).setForeground(self.colors[int(RSCP_Dict[hero][0][0]) - 1])
            self.tableWidget.item(row, 4).setForeground(self.colors[int(RSCP_Dict[hero][0][0]) - 1])
            row += 1

        # Styling and positioning
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.tableWidget.setColumnWidth(0, 26)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 30)
        self.tableWidget.move(15, 200)
        self.tableWidget.resize(422, 500)
        p = self.tableWidget.palette()
        p.setColor(QPalette.Base, QColor(12, 12, 12))
        self.tableWidget.setPalette(p)
        self.font.setPointSize(11)
        self.tableWidget.horizontalHeader().setFont(self.font)
        self.tableWidget.setFont(self.font)


        # Creates the progressbar for when Scan is running
        self.progressbar = MyProgressBar()
        self.progressbar.setRange(0, 0)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setFixedSize(700, 70)
        self.progressbar.move(700, -10)

        # Creates helper text on GUI
        self.label = QLabel(self)
        self.label.setText("Mouse interval length (second):")
        self.label.move(250, 890)
        self.label2 = QLabel(self)
        self.label2.setText(
            "Set time intervals between camera flicks.\nRecomendations: - 0.6 with dynamic fog\n                             -0.3 without")
        self.label2.move(240, 905)

        # Creates box to enter camera flicks interval
        self.editbox = QLineEdit(self)
        self.editbox.setFixedSize(25, 25)
        self.editbox.setPlaceholderText("0.6")
        self.editbox.installEventFilter(self)
        self.editbox.move(405, 879)

        # Sets main GUI's position
        self.setWindowTitle("Autochess Probability and Probability Tracker")
        self.setFixedSize(450, 980)
        self.setGeometry(1, 24, 450, 980)

    # Opens Tips and Strategies window when its button is clicked
    def show_strat(self):
        self.Strategies.show()
        return

    # Opens and searches for the corresponding keyword when its cell is clicked
    def onTableClicked(self, index):
        if str(index.data()).startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            return
        data = "(cat) " + index.data()
        print(data)
        self.Strategies.show()
        self.Strategies.TextBody.setFocus()
        self.Strategies.TextBody.moveCursor(QTextCursor.End)
        self.Strategies.TextBody.find(data, QTextDocument.FindBackward)

    # Saves new timesleep when edit box is out of focus
    def eventFilter(self, source, event):
        if (event.type() == QEvent.FocusOut and
                source is self.editbox):
            global timesleep
            timesleep = float(self.editbox.text())
            print(timesleep, type(timesleep))
        return super(Myapp, self).eventFilter(source, event)

    # Show Predictions button creates a new thread and starts
    def show_predictions(self):
        self.thread = Show_Predictions_Thread()
        self.thread.start()

    # Scan button creates a new thread and starts, catching 4 signals and connecting them to their appropriate slots
    def Scan(self):
        self.thread = ScanThread()
        self.thread.start()
        self.thread.dota_not_found.connect(self.print_not_found_error)
        self.thread.update_progress.connect(self.update_progress_bar)
        self.thread.finished.connect(self.progress_bar_finished)
        self.thread.thread_complete_RSCP.connect(self.update_RSCP_table)
        self.thread.thread_complete_CAS.connect(self.update_CAS_table)

    # Show errors message when Dota 2 is not found
    def print_not_found_error(self, str):
        QMessageBox.information(self, "Error", str)

    # progress bar changes its text during scanning process
    def update_progress_bar(self, str):
        self.progressbar.setText(str)
        self.progressbar.setVisible(True)

    # progress bar hide itself when scanning is done
    def progress_bar_finished(self):
        self.progressbar.setVisible(False)

    # chesspieces table gets updated using data sent from Scan thread
    def update_RSCP_table(self, Dict):
        row = 0
        for hero in Dict:
            item4 = QTableWidgetItem()
            item4.setData(Qt.EditRole, QVariant(Dict[hero][4]))
            self.tableWidget.setItem(row, 4, item4)
            self.tableWidget.item(row, 4).setForeground(self.colors[int(Dict[hero][0][0]) - 1])
            row += 1

    # class and species table gets updated using data sent from Scan thread
    def update_CAS_table(self, CAS_dict_copy):
        row = 0
        for CAS in CAS_dict_copy:
            self.CAS_tableWidget.setItem(row, 0, QTableWidgetItem(CAS))
            item1 = QTableWidgetItem()
            item1.setData(Qt.EditRole, QVariant(CAS_dict_copy[CAS][0]))
            self.CAS_tableWidget.setItem(row, 1, item1)
            item2 = QTableWidgetItem()
            item2.setData(Qt.EditRole, QVariant(CAS_dict_copy[CAS][1]))
            self.CAS_tableWidget.setItem(row, 2, item2)
            self.CAS_tableWidget.item(row, 0).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 1).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 1).setForeground(Qt.white)
            self.CAS_tableWidget.item(row, 2).setTextAlignment(Qt.AlignHCenter)
            self.CAS_tableWidget.item(row, 2).setForeground(Qt.white)
            row += 1


"""
Creates a worker thread for the Scan button
"""
class ScanThread(QThread):
    # Creates 4 signals with their data type to be sent later
    update_progress = pyqtSignal(str)
    thread_complete_RSCP = pyqtSignal(dict)
    thread_complete_CAS = pyqtSignal(dict)
    dota_not_found = pyqtSignal(str)
    def run(self):
        # Sends error signal if Dota 2 is not found
        try:
            dota = getWindowsWithTitle("Dota 2")[0]
            dota.activate()
        except IndexError as error:
            self.dota_not_found.emit("Can only be used in Dota 2 Autochess")
            return

        # Sends progress bar current progress
        self.update_progress.emit("Occupying mouse for taking images, please don't use it...")

        # Goes to to top right corner of the map, takes screenshot of players' status, template matches to see if they
        # have been eliminated
        time.sleep(0.2)
        pyautogui.click(x=347, y=798)
        pyautogui.click(x=348, y=798)
        pyautogui.click(x=349, y=798)
        pyautogui.click(x=347, y=798)

        os.chdir("C:/autochess_data")
        screenshot = pyautogui.screenshot()
        screenshot = np.asarray(screenshot)
        player_status_list = [screenshot[438:449, 1705:1754], screenshot[525:536, 1705:1754], screenshot[613:624, 1705:1754], screenshot[701:712, 1705:1754], screenshot[788:799, 1705:1754],
                              screenshot[875:886, 1705:1754]]

        failed_icon = cv2.imread("C:/autochess_data/failed_icon.png")
        transparent_failed_icon = cv2.imread("C:/autochess_data/transparent_failed_icon.png")

        num_of_lost_players = 0
        for i in range(0, len(player_status_list)):
            if max(cv2.matchTemplate(player_status_list[i], failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8 or max(
                    cv2.matchTemplate(player_status_list[i], transparent_failed_icon, cv2.TM_CCOEFF_NORMED)) > 0.8:
                num_of_lost_players = 6 - i
                break

        # Takes screenshot of the information table
        press_and_release("f3")
        time.sleep(0.5)
        on_stage_heroes = pyautogui.screenshot()
        press_and_release("f3")
        on_stage_heroes.save("on_stage_heroes.png")
        time.sleep(0.3)

        # Goes to chess boards and takes screenshot, skips players who have lost
        count = 0
        pyautogui.click(x=1602, y=233)
        pyautogui.click(x=1602, y=233)
        time.sleep(timesleep)
        img = pyautogui.screenshot(region=(527, 619, 848, 212))
        count += 1
        img.save(f"{count}.jpg")

        pyautogui.click(x=1602, y=320)
        pyautogui.click(x=1602, y=320)
        time.sleep(timesleep)
        img = pyautogui.screenshot(region=(527, 619, 848, 212))
        count += 1
        img.save(f"{count}.jpg")

        if num_of_lost_players < 6:
            pyautogui.click(x=1602, y=409)
            pyautogui.click(x=1602, y=409)
            time.sleep(timesleep)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.jpg")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 5:
            pyautogui.click(x=1602, y=497)
            pyautogui.click(x=1602, y=497)
            time.sleep(timesleep)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.jpg")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        if num_of_lost_players < 4:
            pyautogui.click(x=1602, y=586)
            pyautogui.click(x=1602, y=586)
            time.sleep(timesleep)
            img = pyautogui.screenshot(region=(527, 619, 848, 212))
            count += 1
            img.save(f"{count}.jpg")
        else:
            img = cv2.imread("C:/autochess_data/Lost.jpg")
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
            img = cv2.imread("C:/autochess_data/Lost.jpg")
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
            img = cv2.imread("C:/autochess_data/Lost.jpg")
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
            img = cv2.imread("C:/autochess_data/Lost.jpg")
            count += 1
            cv2.imwrite(f"{count}.jpg", img)

        # Sends progress bar current progress
        self.update_progress.emit("Feeding images through a neural network...")

        os.chdir("G:/darknet/")

        # Feeds images to neural net
        os.system("G:/darknet/darknet.exe detector test G:\darknet/obj.data G:/darknet/thresh_cfg.cfg G:\darknet/backup/yolov4-obj_25000.weights -ext_output -dont_show -out result.json < data/train.txt")

        # Parses neural net json result
        data = json.load(open("G:/darknet/result.json"))
        all_chess_pieces_list = ([], [], [], [], [], [], [], [])
        for i in range(8):
            for hero in data[i]["objects"]:
                all_chess_pieces_list[i].append(hero["name"])

        # Sends progress bar current progress
        self.update_progress.emit("Template matching icons and tabulating results")

        # Template matches characters' icons and levels' icons to figure out which ones are being held by whom
        on_stage_heroes = cv2.imread("C:/autochess_data/on_stage_heroes.png")
        on_stage_heroes_grayed = cv2.cvtColor(on_stage_heroes, cv2.COLOR_BGR2GRAY)
        temp_on_stage_list = ([], [], [], [], [], [], [], [])
        os.chdir("C:/autochess_data/")
        count3 = 0
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

        # Saves results to global variables so other functions can use them
        global to_show_list
        to_show_list = all_chess_pieces_list
        global on_stage_list
        on_stage_list = temp_on_stage_list

        # tabulates results to a dict
        flat_list = [item for sublist in all_chess_pieces_list for item in sublist]
        RSCP_Dict_Copy = copy.deepcopy(RSCP_Dict)

        for hero in flat_list:
            if hero.endswith("2"):
                RSCP_Dict_Copy[hero[:-1]][4] -= 3
            elif hero.endswith("3"):
                RSCP_Dict_Copy[hero[:-1]][4] -= 9
            else:
                RSCP_Dict_Copy[hero][4] -= 1

        # Emits dict signal carrying new chesspieces table information back to caller function
        self.thread_complete_RSCP.emit(RSCP_Dict_Copy)

        # Template matches classes, species and their numbers icons and tabulates result in a dict
        CAS_dict_copy = copy.deepcopy(CAS_dict)
        on_stage_CAS_icons = on_stage_heroes[
                             on_stage_CAS_y_coors[7 - num_of_lost_players][0]:on_stage_CAS_y_coors[7 - num_of_lost_players][
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
                        if cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED) > 0.7:
                            result_list.append((icon[0], cv2.matchTemplate(number_icon, icon[1], cv2.TM_CCOEFF_NORMED)))
                    result_list = sorted(result_list, key=lambda icon: icon[1], reverse=True)
                    try:
                        CAS_dict_copy[CAS[0]][1] += result_list[0][0]
                    except IndexError as e:
                        print(CAS)
                        print(CAS_dict_copy[CAS[0]][1])
                        print(result_list[0][0])


        # Emits dict signal carrying new class and species table information back to caller function
        self.thread_complete_CAS.emit(CAS_dict_copy)

"""
Creates a worker thread for the Show Predictions button
"""
class Show_Predictions_Thread(QThread):
    def run(self):
        try:
            HEIGHT = 212
            WIDTH = 848
            COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255), (0, 0, 255), (255, 255, 255),
                      (125, 0, 255), (255, 0, 125), (125, 255, 0), (0, 255, 125), (0, 125, 255), (255, 125, 0),
                      (125, 75, 0),
                      (0, 75, 125), (0, 125, 75), (75, 125, 0), (75, 0, 125), (125, 0, 75)]
            data = json.load(open("G:/darknet/result.json"))
            on_stage_img = cv2.imread("C:/autochess_data/on_stage_heroes.png")
            first_half = np.zeros((0, 1160, 3), dtype=np.uint8)
            second_half = np.zeros((0, 1160, 3), dtype=np.uint8)
            os.chdir("C:/autochess_data")
            for i in range(0, len(data)):
                img = cv2.imread(f"C:/autochess_data/{i + 1}.jpg")
                for hero in data[i]['objects']:
                    x_start = round(
                        hero["relative_coordinates"]["center_x"] * WIDTH - hero["relative_coordinates"][
                            "width"] * WIDTH / 2)
                    x_end = round(
                        hero["relative_coordinates"]["center_x"] * WIDTH + hero["relative_coordinates"][
                            "width"] * WIDTH / 2)
                    y_start = round(
                        hero["relative_coordinates"]["center_y"] * HEIGHT - hero["relative_coordinates"][
                            "height"] * HEIGHT / 2)
                    y_end = round(
                        hero["relative_coordinates"]["center_y"] * HEIGHT + hero["relative_coordinates"][
                            "height"] * HEIGHT / 2)
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
            cv2.imwrite("C:/autochess_data/all_predictions.png", all_predictions)
            os.system("C:/autochess_data/all_predictions.png")
        except IndexError as error:
            os.system("C:/autochess_data/all_predictions.png")

App = QApplication([])
window = Myapp()
window.show()
sys.exit(App.exec())
