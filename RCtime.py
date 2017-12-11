import RPi.GPIO as GPIO, time, os
from test import findmood
import pygn
from pygn import createRadio
import pygame
import time
 
DEBUG = 1
GPIO.setmode(GPIO.BCM)
 
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
 
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

def average(arr):
        sum1 = 0
        for i in range(len(arr)):
                sum1 += arr[i]
        return sum1/len(arr)        
     

def averagelight():
        arr = []
        for i in range(25):
                if RCtime(18) >= 50 and RCtime(18) <= 1000:
                        arr.append(87.5)
                if RCtime(18) > 1000 and RCtime(18) <= 2000:
                        arr.append(62.5)
                if RCtime(18) > 2000 and RCtime(18) <= 3000:
                        arr.append(37.5)
                if RCtime(18) > 3000 and RCtime(18) <= 4000:
                        arr.append(12.5)
                if RCtime(18) > 4000:
                        arr.append(5)
        return average(arr)

def moodscore():
        score = averagelight()
        mood = 0
        # Mood calculation formula
        pygame.init()
        if score >= 0 and score <= 25:
                mood = '42948' # somber
                pygame.mixer.music.load("./Songs/To-Build-a-Home-The-Cinematic-Orchestra-Lyrics.wav")
                pygame.mixer.music.play()
                time.sleep(30)
        if score >= 25 and score <= 50:
                mood = '65322' # Peaceful
                pygame.mixer.music.load("./Songs/Michelle-Beatles-Cover-Herb-Alpert.wav")
                pygame.mixer.music.play()
                time.sleep(30)
        if score >= 50 and score <= 75:
                mood = '65330' # Rowdy
                pygame.mixer.music.load("./Songs/Josh-Turner-Your-Man.wav")
                pygame.mixer.music.play()
                time.sleep(30)
        if score >= 75 and score <= 100:
                mood = '42960' # Excited
                pygame.mixer.music.load("./Songs/Eminem-Berzerk-Official-Explicit.wav")
                pygame.mixer.music.play()
                time.sleep(30)
        return findmood(mood)
                
print(moodscore())