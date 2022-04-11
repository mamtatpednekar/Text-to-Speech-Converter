# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:23:17 2022

@author: Mamta Pednekar
"""
from gtts import gTTS
import os
open('text.txt','r').read()
audioOfFile = gTTS(text = text, lang= 'en', slow=False)
audioOfFile.save('audioOfFile.mp3')
os.system("start audioOfFile.mp3")