import pyscreenshot as ImageGrab
import random
from ftplib import FTP
from tkinter import *
import tkinter.messagebox
import os
from PIL import Image, ImageTk

class screenCapturingMainClass():

    filePathForTakenPicture = "Fullscreen/Image.png" #By Default :)

    def takeFullScreenShoot(self):
        im = ImageGrab.grab()
        im.show()

    #takeFullScreenShoot()

    def saveFullScreenShoot(self):
        randomNumber = random.randrange(1, 1000)
        #print(randomNumber)
        fileName = "Fullscreen/Image_" + str(randomNumber) + ".png"
        #print(fileName)
        im = ImageGrab.grab_to_file(fileName)

    def captureSelectedPlaceInScreen(self):
        None

    def saveFullScreenOnServer(self):

    #First try to minimize GUI :)
        root.wm_state('iconic')

        try:

            #Connect to FTP
            ftp = FTP("Your FTP server adress")
            ftp.login("username", "password]")
            print("Connection Succesfull!")
            ftp.cwd("/var/www/html/imageCasts")#Directory, where pictures will be save
            print(ftp.dir())#For printing directiory...

            #Take a picture
            randomNumber = random.randrange(1, 1000)
            filePathForTakenPicture = fileName = "Image_" + str(randomNumber) + ".png"
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
            print(EXCEPTION)
            ftp.close()

            #Unhide Programm GUI
            root.deiconify()

    def deletePictureFromServer(self):

         nameForDeletingPicture = secondPictureName.get()
         print("Name: " + nameForDeletingPicture)

         if nameForDeletingPicture is "":
            tkinter.messagebox.showerror("Picture deleting error!",
                                          "Problem deleting picture, try again latter!")
            return


         try:
            #Connect to FTP
            ftp = FTP("Your FTP server adress")
            ftp.login("username", "password]")
            print("Connection Succesfull!")
            #Move to Picture directory
            ftp.cwd("/var/www/html/imageCasts")
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

class extraFunctionsForClass():

    def printAbout(self):
        print("Made with Love! :)")
        root = Tk()

        root.title("Simple ScreenCapturing - About")
        root.geometry("200x100")

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
root.geometry("500x300")

#Frame

#app = Frame(root)
#app.grid()
#app.pack()

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
#button1.pack(fill="both", pady=20)
#button1.pack(side=RIGHT)


#entry_1 = Entry(root) = Ievades (Input) logs
#ko_velies.grid(row=0, column=1, sticky=E) Sticky novietojums, EAST,WEST, lalala
#ko_velies2.grid(columnspan = 2),aiznem vairakas kollonas
#button_1.bind("<Button-1>", printejuVardu) #Lai pieskirtu metodi konkretai pogai

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
button2.grid(row = 0, column = 0, columnspan=10, rowspan=10)
button2["command"] = extraFunctions.printAbout
#button2.pack(side = LEFT)

fourthMiddleFrame = Frame(root)
fourthMiddleFrame.pack(fill = "both", padx= 5,pady=2)

button4 = Button(fourthMiddleFrame, text = "Delete Lattest Picture")
button4.grid(row = 9)
button4["command"] = captureScreen.deletePictureFromServer

#thirdMiddleFrame = Frame(root)
#thirdMiddleFrame.pack(fill = "both", padx= 5,pady=2) #padx=220, pady=5)
button3 = Button(secondMiddleFrame, text = "Exit")
button3.grid(row = 0, column=25, columnspan=50, rowspan=50)
button3["command"] = extraFunctions.exitApplication



#Also for Picture =)


#image_pil = Image.open("Fullscreen/Image.png").resize((600, 400)) #<-- resize images here


#button3.bind("<Button-1>", exitApplication)
#button3["command"] = extraFunctionsForClass.exitApplication

#Image
#photo = PhotoImage(file=photoURL)
#image = Image.open(photoURL)
#image = image.resize((250, 250), Image.ANTIALIAS)
#image = open(photoURL)

#photo = PhotoImage(file="Fullscreen/Image.png")

#mint = StringVar()
#mint.set(PathTest)

#extraText = self.linkDisplayVariable.set(PathTest)

#photo = PhotoImage(file=picturePathReal)
#photoLabel = Label(root, image=photo, width=200, height=200)
#photoLabel.pack()

#event loop


def updateLinkBox(fullPathToUpdate, directorForPicture):

    prefabForURL = "http://188.226.139.74/imageCasts/"

    linkDisplayVariable.set(prefabForURL+fullPathToUpdate)

    secondPictureName.set(fullPathToUpdate)
    localPathToPicture.set(directorForPicture)

    print("Path to Picture:" + directorForPicture)

    change_picture(localPathToPicture.get())
    #boolTest = True
    #photo = localPathToPicture.get()

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

#root.bind("<Button-1>", callback)

#photoLabel.pack(padx=110, pady=10)#photoLabel.pack(padx=110, pady=10)

#updateLinkBox("Filne")
print("App IS GOING")

root.mainloop()

#saveFullScreenShoot()

#For Auto Capturing, now creating a GUI
#saveFullScreenOnServer()
