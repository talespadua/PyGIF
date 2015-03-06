__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os
from Tkinter import *
import tkMessageBox, tkFileDialog

def add_images(root, images):
    files = tkFileDialog.askopenfilenames(parent=root, title='Choose a File', filetypes=[("Image files", "*.jpg")])
    files = root.tk.splitlist(files)
    if files is not None:
        for f in files:
            try:
                image = PIL.Image.open(f)
                images.append(image)
            except:
                print "deu ruim"


def doNothing():
    print("Lerolero")

def printimages(images):
    print images

def create_menu(root):
    menu = Menu(root)

    return menu

def add_new_subMenu(menu, images):
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New", command=lambda: printimages(images))
    subMenu.add_command(label="Select Images", command=lambda: add_images(menu, images))
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)


def add_toolbar(root, images):
    toolbar = Frame(root, borderwidth = 3, relief = RIDGE)
    add_images_button = Button(toolbar, text="Select Images", command=lambda: add_images(root, images))
    print_imagenames_button = Button(toolbar, text="Print Image Names", command=lambda: printimages(images))
    writegifbutton = Button(toolbar, text="WriteGif", command=doNothing)

    add_images_button.pack(side=LEFT, padx=2, pady=2)
    print_imagenames_button.pack(side=LEFT, padx=2, pady=2)
    writegifbutton.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

# def add_save_gif_button(filename, images, du):
#     save_gif_button

def main():
    images = []
    root = Tk()
    root.geometry("500x500")

    menu = create_menu(root)
    root.config(menu=menu)

    add_new_subMenu(menu, images)

    add_toolbar(root, images)
    root.mainloop()


    #*********** GIF PART**********************
    file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

    filename = "mari_monkey.GIF"
    writeGif(filename, images, duration=0.2)

    #*********** END GIF PART *****************

if __name__ == "__main__":
    main()