import os
import sys

if len(sys.argv)>1:
    None
else:
    #File = input("Which Python script to EXE?")
    Filename = "D:\Python_Projects\Screen_shoot_maker\SimpleTest.py"
    os.system("C:/Python34/Scripts/cxfreeze" + Filename)
    print("Ir")