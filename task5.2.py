import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
REDled = LED(24)
GREENled = LED(25)
YELLOWled = LED(23)


mywin = Tk()
mywin.title("TRAFFIC LIGHTS")
myFont = tkinter.font.Font(family = "Georgia", size = 22, weight = "bold")
mywin.minsize(540, 420)
mywin.configure(bg = "black")

def REDledSwitch():
    if REDled.is_lit:
        REDled.off()
    else:
        REDled.on()
def GREENledSwitch():
    if GREENled.is_lit:
        GREENled.off()
    else:
        GREENled.on()
def YELLOWledSwitch():
    if YELLOWled.is_lit:
        YELLOWled.off()
    else:
        YELLOWled.on() 

botton1= Button(mywin, text = "Red On", font = myFont, command = REDledSwitch, bg = "red" , height = 2, width = 10)
botton1.grid(row = 2, column = 5)

botton2= Button(mywin, text = "Green On", font = myFont, command = GREENledSwitch, bg = "green" , height = 2, width = 10)
botton2.grid(row = 3, column = 5)

botton3= Button(mywin, text = "Yellow On", font = myFont, command = YELLOWledSwitch, bg = "yellow" , height = 2, width = 10)
botton3.grid(row = 4, column = 5)
  
