import pyautogui
import time
import math
import os

# load constants to ram
first_characters_coordinate = (124, 100)
distance_between_columns = 80
distance_between_rows = 130
shows_3D_model_coordinate = (1400, 260)
camera_positions = ((40, 916), (46, 916), (52, 916), (55, 916), (58, 916), (63, 916), (66, 916), (70, 916))
image_region = (527, 619, 848, 212)
all_characters = ('Abaddon', 'Alchemist', 'Axe', 'BeastMaster', 'Panda', 'Chaos', 'Nyx', 'Mirana', 'Razor', 'Morphling','Clock','Doom','Barathum', 'Batrider', 'BH', 'Brood', 'Chen', 'CM', 'DarkWillow', 'Dazzle', 'Disruptor', 'DragonKnight', 'Drow','EarthShaker', 'EarthSpirit', 'Elder', 'EmberSpirit', 'Enchantress', 'Enigma', 'Grandma', 'Grim', 'Gyro', 'Huskar','IceDuck', 'Invoker', 'IO', 'Jakiro', 'Juggernaut', 'KOTL', 'Kunkka', 'LC', 'LoneDruid', 'Leshrac', 'Lich', 'Lina','Lion', 'Luna', 'Lycan', 'Mars', 'Medusa', 'Meepo', 'MonkeyKing', 'AM', 'Necrophos', 'Nevermore', 'NP', 'OgreMagi','OmniKnight', 'Oracle', 'PhuongAnh', 'Pudge', 'QOP', 'SandKing', 'SD', 'ShadowShaman', 'Sladar', 'Slark','Sniper', 'Storm', 'Sven', 'TB', 'Tide', 'Timber', 'Tiny', 'TramAnh', 'Treant', 'Troll', 'Tuskar', 'Undying','Ursa', 'Venom', 'Viper', 'Visage', 'Void', 'VoidSpirit', 'WindRanger', 'Zeus', 'Tinker', 'WitchDoctor','Terrorist', 'Rubik')


# creates separate folders for each character
for character in all_characters:
    try:
        os.mkdir("G:/all_characters/" + character)
    except OSError as error:
        pass


# iterates through all characters
for i in range(len(all_characters)):

    # identify which row we are currently at (each row has 17 characters)
    row = math.floor(i/17)

    # calculates character's coordinate
    coordinate = first_characters_coordinate[0] + i * distance_between_columns, \
                 first_characters_coordinate[1] + distance_between_rows * row

    # mouse clicks to select character
    pyautogui.click(coordinate)
    time.sleep(0.5)

    # mouse clicks to select "shows character's 3D model"
    pyautogui.click(shows_3D_model_coordinate)
    time.sleep(3)

    # iterates through all camera positions, we want to take 20 pictures for each position
    for j in range(len(camera_positions)*20):

        # selects camera position and takes a picture
        pyautogui.click(camera_positions[math.floor(j/20)])
        img = pyautogui.screenshot(region=image_region)

        # changes directory to the current character folder and saves screenshot
        os.chdir("G:/all_characters/" + all_characters[i])
        img.save(all_characters[i] + "_pos_" + str(math.floor(j/20) + 1) + "_" + str(f"{j%20:02d}") + ".png")
        time.sleep(0.2)