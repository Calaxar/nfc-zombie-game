#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO
from pirc522 import RFID
from time import sleep
from getpass import getpass
import os
from random import randint
from challenges import CHALLENGES
from difflib import get_close_matches

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def printZombies() :
    print(" ________  __  __ ____ ___ _____ ____ ")
    print("|__  / _ \|  \/  | __ )_ _| ____/ ___| ")
    print("  / / | | | |\/| |  _ \| ||  _| \___ \ ")
    print(" / /| |_| | |  | | |_) | || |___ ___) |")
    print("/____\___/|_|  |_|____/___|_____|____/ ")

def clear() :
    os.system('clear')
    printZombies()
    print("----------------------------------------------------------------")
    print("Figures found: " + str(numFigsFound) + " | Figures remaining: " + str(figNum - numFigsFound))
    print("----------------------------------------------------------------")

def loadCure() :
    loadingProgress = [1, 10, 30, 70, 90, 99, 100]
    print("All required figures found!")
    print("Loading cure...")
    sleep(1)
    for x in loadingProgress :
        clear()
        print("Loading cure... " + str(x) + "%")
        sleep(randint(1, 3))
    print("CURE UNLOCKED: {}".format(cure))
    
def startCountdown() :
    for x in range(0, 10) :
        clear()
        print("Starting in... " + str(10 - x))
        sleep(1)
    
def runChallenge(challenges) :
    challengeKey = challenges[randint(0, len(challenges))]
    inputAns = ""
    answer = CHALLENGES[challengeKey]
    print("CHALLENGE")
    while inputAns != answer :
        inputAns = str.lower(raw_input(challengeKey + ": "))
        if inputAns != answer : 
            if get_close_matches(inputAns, [answer], 1, 0.66) :
                print("Close! Try again.")
            else :
                print("Incorrect. Try again.")
            sleep(0.5)
    return challengeKey

rc522 = RFID()

numFigsFound = 0
figsFound = []
challenges = list(CHALLENGES.keys())

print("NFCZombies Initialising...")
print("Setup:")
figNum = input("How many figurines need to be found?: ")
cure = getpass(prompt="What's the secret cure?: ", stream=None)
print("Starting in...")
sleep(1)
startCountdown()
clear()
print("Go!!!")
sleep(5)
print("Ready to scan figure...")
while numFigsFound < figNum :
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error : 
        (error, uid) = rc522.anticoll()

        if not error :
            if uid in figsFound :
                print("Figure has already been registered, find a new one!")
            else:
                figsFound.append(uid)
                clear()
                print("New figure registered.")
                challenges.remove(runChallenge(challenges))
                numFigsFound += 1
                print("Correct! Figures remaining: {}".format(figNum - numFigsFound))
                sleep(1)
                clear()
                if numFigsFound < figNum :
                    print("Ready to scan next figure...")
                else :
                    loadCure()
            sleep(1)