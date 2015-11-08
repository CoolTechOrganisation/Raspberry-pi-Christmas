import time
import RPI.GPIO as GPIO

print("Program is Starting ...")
print("Pleas wait ...")
time.sleep(20)

GPIO.setmode(GPIO.Board)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(11, GPIO.LOW)
def Binketen():
for i in range(10):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
def Blinkonce():
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)

def SantaClaus():

#TODO:ADD SANTA CLAUS FONCTION 
    GPIO.cleanup()
