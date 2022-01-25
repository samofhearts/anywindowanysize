from turtle import seth
import pygetwindow
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import ctypes
from ctypes import wintypes


## Global Variables
processList = []
optionList = []

def applyIt():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()
    setHeight = heightEntry.get()
    setWidth = widthEntry.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.size = (int(setWidth), int(setHeight))
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.size = (int(setWidth), int(setHeight))

def minusOnePercent():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.size = (int(wind.width - (wind.width * 0.01)), int(wind.height - (wind.height * 0.01)))
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.size = (int(win.width - (win.width * 0.01)), int(win.height - (win.height * 0.01)))

def plusOnePercent():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.size = (int(wind.width + (wind.width * 0.01)), int(wind.height + (wind.height * 0.01)))
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.size = (int(win.width + (win.width * 0.01)), int(win.height + (win.height * 0.01)))

def moveUp():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.move(0,-10)
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.move(0,-10)

def moveDown():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.move(0,10)
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.move(0,10)

def moveLeft():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.move(-10,0)
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.move(-10,0)

def moveRight():
    global clicked
    global heightEntry
    global widthEntry
    global processList
    global optionList
    selectedWindow = clicked.get()

    if (len(pygetwindow.getWindowsWithTitle(selectedWindow))) > 1:
        for each in processList:
            if each.title == str(selectedWindow):
                for wind in pygetwindow.getWindowsWithTitle(selectedWindow):
                    if wind.left == each.left and wind.top == each.top and wind.width == each.width and wind.height == each.height and wind.title == each.title:
                        wind.move(10,0)
    else:
        win = pygetwindow.getWindowsWithTitle(selectedWindow)[0]
        win.move(10,0)


## Get Process Options
##print(pygetwindow.getAllWindows())

processList = pygetwindow.getAllWindows()

for each in processList:
    ##print(each)
    if(len(str(each.title)) < 1):
        pass
    else:
        optionList.append(each.title)

## Make GUI Window
master = Tk()
master.title('Any Window Any Size')
master.geometry('500x350')

## Set Background Stuff
bgCanvas = Canvas(master,bg="black",width=500, height=350)
background_image = Image.open('background.png')
tkImage = ImageTk.PhotoImage(background_image)
background_label = Label(master, image=tkImage)
background_label.place(x=0,y=0, relwidth=1, relheight = 1)

## Blank Rows / buffers
master.grid_rowconfigure(0,minsize=50)
master.grid_rowconfigure(2,minsize=20)
master.grid_rowconfigure(5,minsize=5)
master.grid_rowconfigure(8,minsize=5)
master.grid_rowconfigure(11,minsize=5)
master.grid_rowconfigure(13,minsize=10)

## Blank Columns / buffers
master.grid_columnconfigure(0,minsize=100)
master.grid_columnconfigure(1,minsize=5)
master.grid_columnconfigure(2,minsize=5)
master.grid_columnconfigure(3,minsize=5)
master.grid_columnconfigure(4,minsize=100)
master.grid_columnconfigure(2,weight=1)

## Title Area
titleText = Label(master, bg='white', text="Any Window Any Size", font=("Times New Roman",16)).grid(row=1, columnspan=5)

## Select Window Dropdown
clicked = StringVar()

windowSelectText = Label(master, bg='white', text="Select Window", font=("Times New Roman",16)).grid(row=3, columnspan=5)
drop = OptionMenu(master, clicked, *optionList)
drop.grid(row=4, column=2)
drop.config(width=40)

## Width Input Box

widthText = Label(master, bg='white', text="Width", font=("Times New Roman",16)).grid(row=6, column=2, sticky=W)
widthEntry = Entry(master, bg='white', width=15, highlightthickness=3)
widthEntry.grid(row=7,column=2, sticky=W)

## Height Input Box
heightText = Label(master, bg='white', text="Height", font=("Times New Roman",16)).grid(row=6, column=2, sticky=E)
heightEntry = Entry(master, bg='white', width=15, highlightthickness=3)
heightEntry.grid(row=7,column=2, sticky=E)

## -1% Button
minusPercentButton = Button(master, bg='white', text="Minus 1 Percent", command = minusOnePercent).grid(row=12, column=2, sticky=W)

## +1% Button
plusPercentButton = Button(master, bg='white', text="Plus 1 Percent", command = plusOnePercent).grid(row=12, column=2, sticky=E)

## move up
moveUpButton = Button(master, bg='white', text="Up", command = moveUp).grid(row=13, column=2, sticky=W)

## move down
moveDownButton = Button(master, bg='white', text="Down", command = moveDown).grid(row=13, column=2, sticky=E)

## move left
moveLeftButton = Button(master, bg='white', text="Left", command = moveLeft).grid(row=14, column=2, sticky=W)

## move right
moveRightButton = Button(master, bg='white', text="Right", command = moveRight).grid(row=14, column=2, sticky=E)

## Apply Button
applyButton = Button(master, bg='white', text="Apply",command = applyIt).grid(row=15, columnspan=5)


## Mainloop keeps tkinter window open
master.mainloop()
