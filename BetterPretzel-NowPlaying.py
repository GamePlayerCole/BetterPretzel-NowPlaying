from urllib.request import urlopen
import threading
import sys

#Defining/Initializng Variables
noSongPlaying = ("Nothing Currently Playing     ")
runLoop = True

while runLoop == True:
    service = input("What streaming service do you use?\n1. Twitch\n2. Mixer\n")
    if service == "1":
        service = "twitch"
        runLoop = False
    elif service == "2":
        service = "mixer"
        runLoop = False
    else:
        print("Invalid input!\n")

runLoop = True

while runLoop == True:
    userName = input("What is your username: ")
    if userName != "":
        runLoop = False
    else:
        print("Invalid Username!\n")

runLoop = True

print("Getting Song info from Pretzel.Rocks...")
url = 'https://www.pretzel.rocks/api/v1/playing/' + service + '/' + userName





#Functions for use in Different Threads.
def checkForNewSong():
    global runLoop
    while runLoop == True:

        urlContents = urlopen(url).read()
        urlArray = urlContents.split()
        stopCount = len(urlArray)
        #Start of Song Name in Array
        index = 2
        songInfo = ""
        currentWord = ""

        while str(urlArray[index]) != "b'->'":
            currentWord = urlArray[index].decode("utf-8")
            songInfo = songInfo + currentWord + " "
            index = index + 1

        currentSongFile = open("currentSong.txt", "r")
        #Checks if currentSong is already in currentSong.txt If it isn't, clears the file.
        if currentSongFile.readline() != songInfo:
            currentSongFile.close()
            #Runs twice; Once for clearing and once for adding the curren song.
            currentSongFile = open("currentSong.txt", "w")
            currentSongFile.write(songInfo)
            currentSongFile.close()

            print(songInfo)

    #Sets the current song to "Nothing Currently Playing"
    currentSongFile = open("currentSong.txt", "w")
    currentSongFile.write(noSongPlaying)
    currentSongFile.close()
    #Closes the Application
    sys.exit()

def exitCheck():
    global runLoop
    while runLoop == True:
        exitInput = input("Type Exit to close: \n")
        if exitInput == "exit" or exitInput == "Exit" or exitInput == "EXIT":
            print("Closing Application...")
            runLoop = False


#Checks for currentSong.txt. If doesn't exist, creates file.
currentSongFile = open("currentSong.txt", "w")
#Used to keep currentSong.txt on "Nothing Currently Playing" until first song is pulled from LastFM
currentSongFile.write(noSongPlaying)
currentSongFile.close()
#Creates Threads for the two functions
newSongThread = threading.Thread(target=checkForNewSong)
exitThread = threading.Thread(target=exitCheck)
newSongThread.start()
exitThread.start()
