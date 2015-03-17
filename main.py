__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os, sys
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


def add_toolbar(root, images, imagename, altura, largura, duracao):
    toolbar = Frame(root, borderwidth = 3, relief = RIDGE)
    add_images_button = Button(toolbar, text="Select Images", command=lambda: add_images(root, images))
    print_imagenames_button = Button(toolbar, text="Print Image Names", command=lambda: printimages(images))
    writegifbutton = Button(toolbar, text="WriteGif", command=lambda: save_gif(imagename, images, altura, largura, duracao))

    #writeGif("teste.gif", images, duration=0.2)

    add_images_button.pack(side=LEFT, padx=2, pady=2)
    print_imagenames_button.pack(side=LEFT, padx=2, pady=2)
    writegifbutton.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

def add_input(root, imagename, altura, largura, duracao):
    nameLabel = Label(root, text="Nome do gif").pack()
    name_input = Entry(root, textvariable=imagename).pack()

    alturaLabel = Label(root, text="Altura").pack()
    altura = Entry(root, textvariable=altura).pack()

    larguraLabel = Label(root, text="Largura").pack()
    largura_input = Entry(root, textvariable=largura).pack()

    duracaoLabel = Label(root, text="FPS (Max 1)").pack()
    duracao_input = Entry(root, textvariable=duracao).pack()

def save_gif(imagename, images, altura, largura, duracao):
    # if altura.get() is not None and largura.get() is not None:

    try:
        int_altura = int(altura.get())
    except:
        int_altura = 500

    try:
        int_largura = int(largura.get())
    except:
        int_largura = 300

    try:
        duracao = float(duracao.get())
        if(duracao > 1):
            duracao = 1
    except:
        duracao = 0.2

    resize_images = []
    for i in images:
        resize_images.append(i.resize((int_largura, int_altura), PIL.Image.ANTIALIAS))
    nome = imagename.get() + ".gif"
    writeGif(nome, resize_images, duration=duracao)
    return

def main():
    images = []
    root = Tk()
    root.title("Gif 4 Me")
    root.geometry("500x500")

    imagename = StringVar(None)
    altura = StringVar(None)
    largura = StringVar(None)
    duracao = StringVar(None)

    menu = create_menu(root)
    root.config(menu=menu)

    add_new_subMenu(menu, images)
    add_toolbar(root, images, imagename, altura, largura, duracao)

    add_input(root, imagename, altura, largura, duracao)
    root.mainloop()

if __name__ == "__main__":
    main()