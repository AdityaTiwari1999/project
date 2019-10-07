#!/usr/bin/python

import subprocess
import pyttsx3
import speech_recognition as sr
#import pyaudio
r = sr.Recognizer()
for i in range(5):
  with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source)
     audio = r.listen(source,timeout=3, phrase_time_limit=3)
try:
 cmd1 = r.recognize(audio)
 print("You said " + cmd1)
except LookupError:
  print("Could not understand audio")
cmd = "locate "
cmd2 = cmd + cmd1
return_str = subprocess.check_output(cmd2, shell = True)
cmd = "xdg-open "
cmd1 = return_str
cmd2 = cmd + cmd1
subprocess.call(cmd2, shell = True)
