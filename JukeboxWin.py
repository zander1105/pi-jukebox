#!/usr/bin/python
# coding: utf-8
import time
import os
import glob
import random
import sys
import vlc

MUSIC_FOLDER ="songs\\"
TUNES = glob.glob(MUSIC_FOLDER+"*.mp4") +  glob.glob(MUSIC_FOLDER+"*.mp3") +  glob.glob(MUSIC_FOLDER+"*.m4a")
if len(TUNES) == 0:
	print("No Tunes in your JukeBox!")
	print("Exiting....")
	sys.exit(1)
else:
	print (str(len(TUNES)) + " songs found in your JukeBox")
for tune in TUNES :
        print( tune );
print ( "playing first song")
player = vlc.MediaPlayer(TUNES[0])
player.play()
print("gear")

while True:
   pass
