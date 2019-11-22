import os, sys
from PIL import Image

verify = 0
while(verify == 0):
  local = input("Qual o diretório da imagem?")
  if local.find(".png") != -1 or local.find(".jpg") != -1 or local.find(".jpeg") != -1:
    verify = 1
  else:
    print("Informe uma imagem em (.jpg, .jpeg, ou .png)")

if verify == 12:
  im1 = Image.open(local)

  height = input("Qual a nova altura da imagem?")
  width = input("Qual a nova largura da imagem?")

  im2 = im1.resize((int(width), int(height)), Image.ANTIALIAS)

  ext = ".png"

  im2.save("out" + ext)
