import pyscreenshot as ImageGrab
import random
from ftplib import FTP

def takeFullScreenShoot():
    im = ImageGrab.grab()
    im.show()

#takeFullScreenShoot()

def saveFullScreenShoot():
    randomNumber = random.randrange(1, 1000)
    #print(randomNumber)
    fileName = "Fullscreen/Image_" + str(randomNumber) + ".png"
    #print(fileName)
    im = ImageGrab.grab_to_file(fileName)

def captureSelectedPlaceInScreen():
    None

def saveFullScreenOnServer():

    try:
        #Connect to FTP
        ftp = FTP("FTP_SERVER")
        ftp.login("USERNAME", "PASSWORD")
        print("Connection Succesfull!")
        ftp.cwd("PATH_WHERE_TO_SAVE")
        print(ftp.dir())#For printing directiory...

        #Take a picture
        randomNumber = random.randrange(1, 1000)
        fileName = "Image_" + str(randomNumber) + ".png"
        print(fileName)
        fileFullPath = "Fullscreen/Image_" + str(randomNumber) + ".png"
        print(fileFullPath)
        im = ImageGrab.grab_to_file(fileFullPath)
        print("Taking picture sucessfull")

        #Open saved Image and store in FTP direction
        #image = open("Fullscreen/Image.png", "rb")
        image = open(fileFullPath, "rb")
        name = fileName
        ftp.storbinary("STOR " + name, image)
        ftp.sendcmd('SITE CHMOD 607 ' + fileName)
        image.close()
        ftp.close()
    except:
        print("Kluuuda")
        ftp.close()

#saveFullScreenShoot()
saveFullScreenOnServer()