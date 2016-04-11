import pyscreenshot as ImageGrab2
import random
from ftplib import FTP
from Tkinter import *
import os
from PIL import Image, ImageTk, ImageGrab
import pyhooked
import pyautogui
import time
import uuid #Use Universally unique identifier for pictures! :D

class screenCapturingMainClass():

    filePathForTakenPicture = "Fullscreen/Image.png" #By Default :)
    clickCount = 0
    windows = []

    mousePositionFirstClickX = 0
    mousePositionFirstClickY = 0
    mousePositionSecondClickX = 0
    mousePositionSecondClickY = 0

    def takeFullScreenShoot(self):
        im = ImageGrab2.grab()
        im.show()

    def saveFullScreenShoot(self):
        randomNumber = random.randrange(1, 10000)
        #print(randomNumber)
        fileName = "Fullscreen/Image_" + str(randomNumber) + ".png"
        #print(fileName)
        im = ImageGrab2.grab_to_file(fileName)

    def captureSelectedPlaceInScreen(self):
        None

    def saveFullScreenOnServer(self):

        #First try to minimize GUI :)
        root.wm_state('iconic')
        #self.takeFullScreenShoot()
        try:

            #Connect to FTP
            ftp = FTP("FTP_server")
            ftp.login("username", "pass")
            print("Connection Succesfull!")
            ftp.cwd("path_where_to_save")
            #print(ftp.dir())#For printing directiory...

            #Take a picture
            randomNumber = random.randrange(1, 1000)
            unique_filename = uuid.uuid4()
            m_words = str(unique_filename).split("-")
            print("After split " + m_words[0])
            filePathForTakenPicture = fileName = m_words[0] + ".png"
            fileFullPath = "Fullscreen/Image_" + str(randomNumber) + ".png"
            print(fileFullPath)
            im = ImageGrab2.grab_to_file(fileFullPath)
            print("Taking picture sucessfull")

            #Open saved Image and store in FTP direction
            #image = open("Fullscreen/Image.png", "rb")
            image = open(fileFullPath, "rb")
            name = fileName
            ftp.storbinary("STOR " + name, image)
            #Priviliges to access a picture
            ftp.sendcmd('SITE CHMOD 607 ' + fileName)
            image.close()
            ftp.close()

            #Show GUI
            #showGUIAfterCapturing()
            #self.deletePictureFromServer(filePathForTakenPicture)

            updateLinkBox(filePathForTakenPicture, fileFullPath)

            #Unhide Programm GUI
            root.deiconify()

            #At and, also show a picture...
            #im.show()
        except:
            print("Kluuuda")
            #print(EXCEPTION)
            ftp.close()

            #Unhide Programm GUI
            root.deiconify()

    def saveAreaScreenShoot(self):
        root.wm_state('iconic')
        print("Area!")
        screenWindow = Tk()
        w, h = screenWindow.winfo_screenwidth(), screenWindow.winfo_screenheight()
        screenWindow.overrideredirect(1)
        screenWindow.geometry("%dx%d+0+0" % (w, h))
        #screenWindow.geometry("1920x1080")
        screenCapturingMainClass.windows.append(screenWindow)
        screenWindow.bind("<Button-1>", leftClick)
        screenWindow.attributes('-alpha', 0.01)
        #root.deiconify()

    def deletePictureFromServer(self):

         nameForDeletingPicture = secondPictureName.get()
         print("Name: " + nameForDeletingPicture)

         if nameForDeletingPicture is "":
            tkinter.messagebox.showerror("Picture deleting error!",
                                          "Problem deleting picture, try again latter!")
            return

         try:
            #Connect to FTP
            ftp = FTP("FTP_server")
            ftp.login("username", "pass")
            ftp.cwd("path_where_to_save")
            #Delete Lattest Picture or specific picture
            ftp.delete(nameForDeletingPicture)

            if localPathToPicture.get() is "":
                None
            else:
                os.remove(localPathToPicture.get())


            #Close FTP connection to server!
            ftp.close()

            change_picture("no_money_no_honey.png")
            linkDisplayVariable.set("")

            tkinter.messagebox.showinfo("Deleting Sucessfull", "Lattest picture have been deleted!")

         except:
            print("Dzesanas procesaa ir radusies kluda")
            ftp.close()

def leftClick(event):

    screenCapturingMainClass.clickCount += 1

    if screenCapturingMainClass.clickCount == 1:
        screenCapturingMainClass.mousePositionFirstClickX = pyautogui.position()
        print(screenCapturingMainClass.mousePositionFirstClickX[0])
        print(screenCapturingMainClass.mousePositionFirstClickX[1])
        #screenCapturingMainClass.mousePositionFirstClickY = root.winfo_pointery()
    elif screenCapturingMainClass.clickCount == 2:
        screenCapturingMainClass.mousePositionSecondClickX = pyautogui.position()
        print(screenCapturingMainClass.mousePositionSecondClickX[0]+113)
        print(screenCapturingMainClass.mousePositionSecondClickX[1])
        screenCapturingMainClass.windows[0].destroy()#destroy capturing window
        #screenCapturingMainClass.windows.clear()#also clear list! :) THIS DOESNT WORK ON Python 2
        screenCapturingMainClass.windows = []

        try:

            #Connect to FTP
            #Connect to FTP
            ftp = FTP("FTP_server")
            ftp.login("username", "pass")
            ftp.cwd("path_where_to_save")
            #print(ftp.dir())#For printing directiory...

            #Take a picture
            randomNumber = random.randrange(1, 1000)
            unique_filename = uuid.uuid4()
            m_words = str(unique_filename).split("-")
            print("After split " + m_words[0])
            filePathForTakenPicture = fileName = m_words[0] + ".png"
            #filePathForTakenPicture = fileName = "Image_" + str(randomNumber) + ".png"
            print(fileName)
            fileFullPath = "Fullscreen/Image_" + str(randomNumber) + ".png"
            print(fileFullPath)
            im=ImageGrab2.grab(bbox=(screenCapturingMainClass.mousePositionFirstClickX[0],
                                screenCapturingMainClass.mousePositionFirstClickX[1],
                                screenCapturingMainClass.mousePositionSecondClickX[0],
                                screenCapturingMainClass.mousePositionSecondClickX[1])).save(fileFullPath)
            print("Taking picture sucessfull")

            #Open saved Image and store in FTP direction
            #image = open("Fullscreen/Image.png", "rb")
            image = open(fileFullPath, "rb")
            name = fileName
            ftp.storbinary("STOR " + name, image)
            #Priviliges to access a picture
            ftp.sendcmd('SITE CHMOD 607 ' + fileName)
            image.close()
            ftp.close()

            #Show GUI
            #showGUIAfterCapturing()
            #self.deletePictureFromServer(filePathForTakenPicture)

            updateLinkBox(filePathForTakenPicture, fileFullPath)

            #Unhide Programm GUI
            root.deiconify()
            #back counter!!! :)
            screenCapturingMainClass.clickCount = 0

            #At and, also show a picture...
            #im.show()
        except:
            print("Kluuuda")
            print(EXCEPTION)
            ftp.close()

            #Unhide Programm GUI
            root.deiconify()
            #Back counter! :)
            screenCapturingMainClass.clickCount = 0

        #screenCapturingMainClass.clickCount = 0

        #root.deiconify()


class extraFunctionsForClass():

    def printAbout(self):

        root = Tk()

        root.title("Simple ScreenCapturing - About")
        root.geometry("200x140")

        #Frame
        app = Frame(root)
        app.grid()

        #label
        label = Label(app, text = "Application Made With Love! :)")
        label.grid()

    def exitApplication(self):
        print("Exiting Application")
        sys.exit()
        #os._exit()


root = Tk()
linkDisplayVariable = StringVar()
picturePathReal = "Fullscreen/Image.png"
pictureName = ""
secondPictureName = StringVar()
secondPictureName.set("no_money_no_honey.png")
localPathToPicture = StringVar()
boolTest = False


root.title("Simple ScreenCapturing")
root.geometry("530x390")

captureScreen = screenCapturingMainClass()
extraFunctions = extraFunctionsForClass()

topFrame = Frame(root)
topFrame.pack()

#label
label = Label(topFrame, text = "ScreenShoot Maker", fg="blue", font=("Arial", 16))
label.grid()

firstMiddleFrame = Frame(root)
firstMiddleFrame.pack(padx= 50, pady=5) #padx=190, pady=15);

#Button
button1 = Button(firstMiddleFrame, text = "Take ScreenShoot", fg="purple")
button1.grid(row = 0)
button1["command"] = captureScreen.saveFullScreenOnServer

previewInfoLabel = Label(firstMiddleFrame, text="Picture Preview:", font=("Arial"))
previewInfoLabel.grid(row=0, column=1, columnspan=2, rowspan=2,
           sticky=W+E+N+S, padx=195, pady=5)

#This will be a TextBox?
textBoxFrame = Frame(root)
textBoxFrame.pack(fill = "both", padx= 5,pady=2)

titleForTextBox = Label(textBoxFrame, text="Link to your Picture: ", font=("Arial", 8))
titleForTextBox.grid(row = 9, column = 0)

entry_1 = Entry(textBoxFrame, textvariable=linkDisplayVariable)
entry_1.grid(row =9, column = 0)

secondMiddleFrame = Frame(root)
secondMiddleFrame.pack(fill="both", padx= 5,pady=2) #padx=215, pady=5)
button2 = Button(secondMiddleFrame, text = "About")
button2.grid(row = 0, column = 0, columnspan=10, rowspan=10, pady = 10)
button2["command"] = extraFunctions.printAbout

fourthMiddleFrame = Frame(root)
fourthMiddleFrame.pack(fill = "both", padx= 5,pady=2)

button4 = Button(fourthMiddleFrame, text = "Delete Lattest Picture")
button4.grid(row = 9)
button4["command"] = captureScreen.deletePictureFromServer

button3 = Button(secondMiddleFrame, text = "Exit")
button3.grid(row = 0, column=25, columnspan=50, rowspan=50, padx = 10, pady = 10)
button3["command"] = extraFunctions.exitApplication

button4 = Button(firstMiddleFrame, text = "Take Area ScreenShoot", fg="purple")
button4.grid(row = 1, column=0)
button4["command"] = captureScreen.saveAreaScreenShoot

def updateLinkBox(fullPathToUpdate, directorForPicture):

    prefabForURL = "URL PREFAB"

    linkDisplayVariable.set(prefabForURL+fullPathToUpdate)

    secondPictureName.set(fullPathToUpdate)
    localPathToPicture.set(directorForPicture)

    print("Path to Picture:" + directorForPicture)

    change_picture(localPathToPicture.get())

    print("MOMENT:" + linkDisplayVariable.get())

file_in = secondPictureName.get()
realImage = secondPictureName.get()

pil_image = Image.open(file_in)

image200x100 = pil_image.resize((250, 150), Image.ANTIALIAS)
file_out = 'Fullscreen/Roses200x100.png'
image200x100.save(file_out)

photo = ImageTk.PhotoImage(image200x100)
photoLabel = Label(firstMiddleFrame, image=photo, width=250, height=150)
photoLabel.grid(row=0, column=1, #columnspan=3, rowspan=3,
            sticky=W+E+N+S, padx=9, pady=5)

def change_picture(image):
    pil_image = Image.open(image)

    image200x100 = pil_image.resize((250, 150), Image.ANTIALIAS)
    file_out = 'Fullscreen/Roses200x100.png'
    image200x100.save(file_out)

    img2 = ImageTk.PhotoImage(image200x100)
    photoLabel.configure(image = img2)
    photoLabel.image = img2

if __name__ == "__main__":
    root.mainloop()
    print("App IS GOING")

