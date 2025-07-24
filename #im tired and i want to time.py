#very good
import time
import random
from plyer import notification
from playsound import playsound
import os
playtime = int(input('how long do you want to play in minutes: ')) * 60
warningtime = int(input('how long will you want to finish up in minutes: ')) * 60
meowlib = [".\\Meow.wav", ".\\Meow2.wav", ".\\Meow3.wav", ".\\Meow4.wav", ".\\Meow5.wav"]
time.sleep(playtime)
playsound(".\\Meow.wav")
notification.notify(title = "THIS IS IT", message = "YOU HAVE BEEN WARNED BEFORE AND NOW YOU MUST DIE", app_icon = None, timeout = 10)
for i in range(9):
    playsound(meowlib[random.randint(0,4)])
notification.notify(title = "", message = "...of cute cats", app_icon = None, timeout = 10)
time.sleep(warningtime)
#murder diablo
#in cold blood

os.system('taskkill /im "Diablo III64.exe"')
notification.notify(title = "ok but srsly", message = "you needed to get off the game like yesterday", app_icon = None, timeout = 10)