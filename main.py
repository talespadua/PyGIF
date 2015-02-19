__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os
from Tkinter import *
import tkMessageBox, tkFileDialog

def add_images(root, images):
    files = tkFileDialog.askopenfilenames(parent=root, title='Choose a File')
    if files is not None:
        for f in files:
            images.append(f)

def doNothing():
    print("Lerolero")

def printimages(images):
    print images

def create_window(root, images):
    menu = Menu(root)
    root.config(menu=menu)
    root.geometry("500x500")
    add_new_subMenu(menu, images)
    add_edit_menu(menu)

def add_new_subMenu(menu, images):
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New", command=lambda: printimages(images))
    subMenu.add_command(label="Select Images", command=lambda: add_images(root, images))
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)


def add_edit_menu(menu):
    editMenu = Menu(menu)
    menu.add_cascade(label="File", menu=editMenu)
    editMenu.add_command(label="New", command=doNothing)
    editMenu.add_command(label="Lero", command=doNothing)
    editMenu.add_separator()
    editMenu.add_command(label="Exit", command=doNothing)

root = Tk()

image_names = []

create_window(root, image_names)

root.mainloop()


#*********** GIF PART**********************
file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

images = [PIL.Image.open(fn) for fn in file_names]

filename = "mari_monkey.GIF"
writeGif(filename, images, duration=0.2)

#*********** END GIF PART *****************
