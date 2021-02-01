# Copyright (c) 2017 Adafruit Industries
# Author: James DeVito
# SH1106 Translator : Mesut Can ALAGÖZ
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import RPi.GPIO as GPIO

import time

import SH1106
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



# Input pins:
L_pin = 5 
R_pin = 26 
C_pin = 13 
U_pin = 6 
D_pin = 19 

A_pin = 16 
B_pin = 20 


GPIO.setmode(GPIO.BCM) 

GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up


# 128x64 display with hardware I2C:
disp = SH1106.SH1106()
disp.Init()

# Clear display.
disp.clear()


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)


try:
    while 1:
        if GPIO.input(U_pin): # button is released
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up
        else: # button is pressed:
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  #Up filled

        if GPIO.input(L_pin): # button is released
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left
        else: # button is pressed:
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  #left filled

        if GPIO.input(R_pin): # button is released
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right
        else: # button is pressed:
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1) #right filled

        if GPIO.input(D_pin): # button is released
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down
        else: # button is pressed:
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1) #down filled

        if GPIO.input(C_pin): # button is released
            draw.rectangle((20, 22,40,40), outline=255, fill=0) #center 
        else: # button is pressed:
            draw.rectangle((20, 22,40,40), outline=255, fill=1) #center filled

        if GPIO.input(A_pin): # button is released
            draw.ellipse((70,40,90,60), outline=255, fill=0) #A button
        else: # button is pressed:
            draw.ellipse((70,40,90,60), outline=255, fill=1) #A button filled

        if GPIO.input(B_pin): # button is released
            draw.ellipse((100,20,120,40), outline=255, fill=0) #B button
        else: # button is pressed:
            draw.ellipse((100,20,120,40), outline=255, fill=1) #B button filled
            #Little easter egg, for you to discover how. :)
        if not GPIO.input(A_pin) and not GPIO.input(B_pin) and not GPIO.input(C_pin):
            ppm = Image.open('happycat_oled_64.ppm').convert('1')
            image.paste(ppm, (0,5))
        else:
            # Display image.
            disp.ShowImage(disp.getbuffer(image))
            
         
        time.sleep(.01) 


except KeyboardInterrupt: 
    GPIO.cleanup()