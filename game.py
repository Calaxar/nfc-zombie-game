#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO
from pirc522 import RFID
from time import sleep
from getpass import getpass
import os
from random import randint

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def clear() : os.system('clear')

def loadCure(cure) :
    print("All required figures found!")
    print("Loading cure...")
    sleep(randint(1, 3))
    print("1%")
    sleep(randint(1, 3))
    print("10%")
    sleep(randint(1, 3))
    print("30%")
    sleep(randint(1, 3))
    print("70%")
    sleep(randint(1, 3))
    print("90%")
    sleep(randint(1, 3))
    print("99%")
    sleep(randint(1, 3))
    print("100%")
    sleep(1)
    print("CURE UNLOCKED: {}".format(cure))
    
def startCountdown() :
    for x in range(0, 10) :
    clear()
    print(10 - x)
    sleep(1)

rc522 = RFID()

numFigsFound = 0
figsFound = []

print("NFCZombies Initialising...")
print("Setup:")
figNum = input("How many figurines need to be found?: ")
cure = getpass(prompt="What's the secret cure?: ", stream=None)
print("Starting in...")
sleep(1)
#startCountdown()
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
                print("New figure registered.")
                ans = ""
                while ans != "yes" :
                    ans = raw_input("Can you answer this question?: ")
                numFigsFound += 1
                print("Correct! Figures remaining: {}".format(figNum - numFigsFound))
                if numFigsFound < figNum :
                    print("Ready to scan next figure...")
                else :
                    #loadCure(cure)
            sleep(1)