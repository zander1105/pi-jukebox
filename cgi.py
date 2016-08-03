#!/usr/bin/python
# coding: utf-8
import time
import os
import glob
import random
import sys

MUSIC_FOLDER = "C:\\Users\\gtafi\\Desktop\\pi-juke-\\songs\\"
TUNES = glob.glob(MUSIC_FOLDER+"*.mp3") +  glob.glob(MUSIC_FOLDER+"*.m4a")
if len(TUNES) == 0:
    print("No Tunes in your JukeBox!")
    print("Exiting....")
    sys.exit(1)
else:
    print (str(len(TUNES)) + " songs found in your JukeBox")

for tune in TUNES :
    print( "<h1><font color=\"06dbo6\">" + tune + "</font></h1>" )
    print(" <video width=\"240\" height=\"200\" controls>" )
    print("<source src=\"" + tune + "\" type=\"video/mp4\">" )
    print("<source src=\"" + tune + "\" type=\"video/ogg\">" )
    print("Your browser does not support the video tag.")
    print("</video>")