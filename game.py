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

# clear the console and reprint the game title, figure details
def clear() :
    os.system('clear')
    printZombies()
    print("----------------------------------------------------------------")
    print("Figures found: " + str(numFigsFound) + " | Figures remaining: " + str(figNum - numFigsFound))
    print("----------------------------------------------------------------")

# imitate a loading screen to add suspense to the final part of the game, and then reveal the secret cure
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
    
# countdown from 10 to 0 at the start of the game
def startCountdown() :
    for x in range(0, 10) :
        clear()
        print("Starting in... " + str(10 - x))
        sleep(1)
    
# picks one of the challenges at random and tests the players with it, returns challenge key
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

# initialise RFID module
rc522 = RFID()

# number of figures the players have found
numFigsFound = 0
# a collection of the serial numbers of figures already scanned; prevents reuse of same figures in game
figsFound = []
# a list of the keys stored in CHALLENGES; used to pick a random challenge for the players
challenges = list(CHALLENGES.keys())

print("NFCZombies Initialising...")
print("Setup:")
figNum = input("How many figurines need to be found?: ")
# getpass prevents the input from being echoed in the console, so the players cant see it
cure = getpass(prompt="What's the secret cure?: ", stream=None)
print("Starting in...")
sleep(1)
startCountdown()
clear()
print("Go!!!")
sleep(3)
print("Ready to scan figure...")
while numFigsFound < figNum :
		# check if a figure is being scanned, returns error if not
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error : 
				# attempt to get figure serial number
        (error, uid) = rc522.anticoll()

        if not error :
						# if already scanned:
            if uid in figsFound :
                print("Figure has already been registered, find a new one!")
						# if not already scanned
            else:
                figsFound.append(uid)
                clear()
                print("New figure registered.")
								# run challenge, and remove it from the selection pool
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