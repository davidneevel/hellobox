# OLEDtext.py

# This Python code is meant for use with the Raspberry Pi and Adafruit's monochrome displays!

# This program is the simplest in the whole repo. All it does is prints 3 'Hello!'s in various forms on the OLED display.
# It illustrates how to change the font size and positioning of text on the OLED... As well as showing how to do
# basic text!

# This program was created by The Raspberry Pi Guy!

# Imports the necessary libraries... Gaugette 'talks' to the display ;-)
import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import sys


import textwrap


#line1 = "balls"
#line2 = "my balls"
#line3 = "balls indeed"
# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128) # Change rows & cols values depending on your display dimensions.


# led.draw_text2(x-axis, y-axis, whatyouwanttoprint, size) < Understand?
# So led.drawtext2() prints simple text to the OLED display like so:
def display(a):
    led.begin()
    led.clear_display()
    led.display()
    #led.invert_display()
    #time.sleep(0.5)
    #led.normal_display()
    #time.sleep(0.5)
    
    wrapped = textwrap.wrap(a, 21)
    lines = len(wrapped)
    text = wrapped[0]
    led.draw_text2(0,0,text,1)
    
    if lines > 1:
        text2 = wrapped[1]
        led.draw_text2(0,8,text2,1)
    if lines > 2:
        text3 = wrapped[2]
        led.draw_text2(0,16,text3,1)
    if lines > 3:
        text4 = wrapped[3]
        led.draw_text2(0,24,text4,1)
    led.display()

def clear():
    led.clear_display()
    led.display()
    
    
if __name__ == "__main__":
    print "es"
    display(line1, line2, line3)
