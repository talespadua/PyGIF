__author__ = 'tales.cpadua'

from images2gif import writeGif
import PIL.Image
import os
from Tkinter import *

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))

images = [PIL.Image.open(fn) for fn in file_names]

filename = "mari_monkey.GIF"
writeGif(filename, images, duration=0.2)