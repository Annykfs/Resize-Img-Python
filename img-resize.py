import os, sys
import Image

local = input("Qual o diretório da imagem?")

im1 = Image.open(local)

height = input("Qual a nova altura da imagem?")
width = input("Qual a nova largura da imagem?")
