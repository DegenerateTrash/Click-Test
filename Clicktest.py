import os, sys
from PIL import Image 
import time, random
from random import randrange
import win32api, win32con
from numpy import *

def screengrab():
    from PIL import ImageGrab
    import time
    time.clock()
    image = ImageGrab.grab()
    for y in range(108, 750, 10):
        for x in range(430, 1420, 10):
            color = image.getpixel((x, y))
            #if color == (range(57,58),range(54,56),range(35,45)):
            if color == (0,255,250):
                win32api.SetCursorPos((x,y))
                x,y = win32api.GetCursorPos()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                #time.sleep(0.00001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                
                print("YeSS")
                return
                
            #if s.getpixel(xy)== (255, 255, 255):
    #print(time.clock())
i = 0
while i != 500:
    screengrab()
    i += 1
    
#while True:
    #s = screengrab()
    #if s.getpixel(xy)== (255, 255, 255):
      #  break
