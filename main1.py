import json

import pygame
from PyQt5.QtWidgets import *

settings = {}


def read_data():
    global settings
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except:
        settings = {
            "skin": "img.png",
            "money": 0
        }
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)


widow = QWidget()
main_line = QVBoxLayout()
start_btn = QPushButton("Старт")



def buy_skin_1():
    read_data()
    if settings["money"] >= 7:
        settings["money"] >= 7
        settings["skin"] = "kartka/asteroid.png"
        write_data()
    else:
        print("Грошей не хветає!!")


