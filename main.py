__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os
from Tkinter import *
import tkMessageBox, tkFileDialog

def add_images(root, images):
    files = tkFileDialog.askopenfilenames(parent=root, title='Choose a File', filetypes=[("Image files", "*.jpg")])
    if files is not None:
        for f in files:
            images.append(f)

def doNothing():
    print("Lerolero")

def printimages(images):
    print images

def create_window(images):
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    root.geometry("500x500")
    add_new_subMenu(menu, images)
    add_edit_menu(menu)
    add_toolbar(root, images)
    root.mainloop()

def add_new_subMenu(menu, images):
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New", command=lambda: printimages(images))
    subMenu.add_command(label="Select Images", command=lambda: add_images(menu, images))
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)


def add_edit_menu(menu):
    editMenu = Menu(menu)
    menu.add_cascade(label="File", menu=editMenu)
    editMenu.add_command(label="New", command=doNothing)
    editMenu.add_command(label="Lero", command=doNothing)
    editMenu.add_separator()
    editMenu.add_command(label="Exit", command=doNothing)

def add_toolbar(root, images):
    toolbar = Frame(root, borderwidth = 3, relief = RIDGE)
    add_images_button = Button(toolbar, text="Select Images", command=lambda: add_images(root, images))
    print_imagenames_button = Button(toolbar, text="Print Image Names", command=lambda: printimages(images))

    add_images_button.pack(side=LEFT, padx=2, pady=2)
    print_imagenames_button.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

def main():


    image_names = []

    create_window(image_names)

    #*********** GIF PART**********************
    file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

    images = [PIL.Image.open(fn) for fn in file_names]

    filename = "mari_monkey.GIF"
    writeGif(filename, images, duration=0.2)

    #*********** END GIF PART *****************

if __name__ == "__main__":
    main()