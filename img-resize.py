import os, sys
from PIL import Image


local = input("Qual o diretório da imagem?")


im1 = Image.open(local)

height = input("Qual a nova altura da imagem?")
width = input("Qual a nova largura da imagem?")

im2 = im1.resize((int(width), int(height)), Image.ANTIALIAS)

ext = ".png"

im2.save("out" + ext)
