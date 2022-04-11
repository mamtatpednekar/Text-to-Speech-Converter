# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from gtts import gTTS
import os
#Importing OS to obtain the OS features for media
text = "Hi Good Morning"
audio = gTTS(text = text, lang= 'en', slow=False)
audio.save('audio.mp3')

os.system("start audio.mp3")
#for MAC, use afplay output.mp3
