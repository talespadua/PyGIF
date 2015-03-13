__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os
from Tkinter import *
import tkMessageBox, tkFileDialog

def add_images(root, images):

    if len(images) > 0:
        while len(images) > 0:
            images.pop()

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


def add_toolbar(root, images, imagename):
    toolbar = Frame(root, borderwidth = 3, relief = RIDGE)
    add_images_button = Button(toolbar, text="Select Images", command=lambda: add_images(root, images))
    print_imagenames_button = Button(toolbar, text="Print Image Names", command=lambda: printimages(images))
    writegifbutton = Button(toolbar, text="WriteGif", command=lambda: save_gif(imagename, images))

    #writeGif("teste.gif", images, duration=0.2)

    add_images_button.pack(side=LEFT, padx=2, pady=2)
    print_imagenames_button.pack(side=LEFT, padx=2, pady=2)
    writegifbutton.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

def add_input(root, imagename):
    nameLabel = Label(root, text="Nome do gif")
    nameLabel.pack()

    name_input = Entry(root, textvariable=imagename)
    name_input.pack()


def save_gif(imagename, images):
    nome = imagename.get() + ".gif"
    writeGif(nome, images, duration=0.2)

def main():
    images = []
    root = Tk()
    root.title("Gif 4 Me")
    root.geometry("500x500")

    imagename = StringVar()

    menu = create_menu(root)
    root.config(menu=menu)

    add_new_subMenu(menu, images)
    add_toolbar(root, images, imagename)

    add_input(root, imagename)

    root.mainloop()


    # #*********** GIF PART**********************
    # file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
    #
    # filename = "mari_monkey.GIF"
    # writeGif(filename, images, duration=0.2)

    #*********** END GIF PART *****************

if __name__ == "__main__":
    main()