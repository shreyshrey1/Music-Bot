# import RPi.GPIO as GPIO, time, os      
 
# DEBUG = 1
# GPIO.setmode(GPIO.BCM)
 
# def RCtime (RCpin):
#         reading = 0
#         GPIO.setup(RCpin, GPIO.OUT)
#         GPIO.output(RCpin, GPIO.LOW)
#         time.sleep(0.1)
 
#         GPIO.setup(RCpin, GPIO.IN)
#         # This takes about 1 millisecond per loop cycle
#         while (GPIO.input(RCpin) == GPIO.LOW):
#                 reading += 1
#         return reading

def average(arr):
        sum1 = 0
        for i in range(len(arr)):
                sum1 += arr[i]
        return sum1/len(arr)        
     

def averagelight():
        arr = []
        for i in range(25):
                if RCtime(18) >= 50 and RCtime <= 1000:
                        arr.append(87.5)
                if RCtime(18) > 1000 and RCtime <= 2000:
                        arr.append(62.5)
                if RCtime(18) > 2000 and RCtime <= 3000:
                        arr.append(37.5)
                if RCtime(18) > 3000 and RCtime <= 4000:
                        arr.append(12.5)
                if RCtime(18) > 4000
                        arr.append(5)
        return average(arr)

def moodscore():
        score = 0
        mood = 0
        # Mood calculation formula

        if score <= 0 and score <= 25:
                mood = 42948
        if score >= 25 and score <= 50:
                mood = 65322
        if score >= 50 and score <= 75:
                mood = 65330
        if score >= 75 and score <= 100:
                mood = 42960
