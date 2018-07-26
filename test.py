from urllib.request import urlopen
import sys
import threading

runLoop = True
#print(str(runLoop))


while runLoop == True:
    service = input("What streaming service do you use?\n1. Twitch\n2. Mixer\nStreaming Service: ")
    if service == "1":
        print("Twitch")
        runLoop = False
    else:
        print("Error")
