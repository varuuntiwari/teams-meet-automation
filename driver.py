from pyautogui import *
from time import sleep
import vars

def driveToClass(day):
    className = 'img\\'+vars.CLASSES[day]
    if(locateCenterOnScreen('img/back.jpg', confidence=0.8) != None):
        x, y = locateCenterOnScreen('img/back.jpg', confidence=0.8)
        click(x, y)
        sleep(2)
    x, y = locateCenterOnScreen(className, confidence=0.8)
    click(x, y, duration=0.5)
    sleep(3)
    print("Class is open now, attempting to join...")
    joinClass()

def checkMic():
    mic = 'img\\mic.jpg'
    if(locateCenterOnScreen(mic, confidence=0.6) != None):
        print("Mic is on, attempting to switch off...")
        x, y = locateCenterOnScreen('img/back.jpg', confidence=0.8)
        click(x, y, duration=0.5)
        print("Mic off...")
    else:
        print("Mic is off, resuming...")

def joinClass():
    if(locateCenterOnScreen('img/join.jpg', confidence=0.8) == None):
        print("Meeting not found, exiting...")
        exit(1)
    else:
        x, y = locateCenterOnScreen('img/join.jpg', confidence=0.8)
    moveTo(x, y)
    click(button='left')
    sleep(2)
    checkMic()
    x, y = locateCenterOnScreen('img/joinnow.jpg', confidence=0.8)
    moveTo(x, y)
    click(button='left')