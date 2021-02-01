# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
# SH1106 Translator: Mesut Can ALAGÖZ

import time
import datetime
import config
import SH1106

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
#RST = None     # on the PiOLED this pin isnt used
# 128x64 display
disp = SH1106.SH1106()

# Clear display.
disp.Init()
disp.clear()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (disp.width, disp.height), "WHITE")
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,disp.width, disp.height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = disp.height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()
font10 = ImageFont.truetype('Font.ttf',9)

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:

    # Draw a black filled box to refresh the image.
    draw.rectangle((0,0,disp.width, disp.height), outline=255, fill=255)

    # $3*100/$2 Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f%%\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Ram: %s/%sMB %s%%\", $3,$2,$5 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    temp = subprocess.check_output(cmd, shell = True )
    timeString = '%H:%M:%S'
    result  = datetime.datetime.now().strftime(timeString)

    # Write two lines of text.

    draw.text((x, top+5),       "IP: " + str(IP,'utf-8'),  font=font, fill=0)
    draw.text((x, top+15),     str(CPU,'utf-8') + " " + str(temp,'utf-8'), font=font, fill=0)
    draw.text((x, top+25),    str(MemUsage,'utf-8'),  font=font, fill=0)
    draw.text((x, top+35),    str(Disk,'utf-8'),  font=font, fill=0)
    draw.text((x, top+45), result, font=font, fill=0)
    draw.text((x, top+55), "Owner:Mesut Can ALAGÖZ ", font=font10, fill=0)

    # Display image.
    disp.ShowImage(disp.getbuffer(image))
    time.sleep(.1)