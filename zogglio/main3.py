from PIL import Image

# Abrir a imagem existente
imageOriginal =  Image.open('panda.jpg')

# fazer a rotação.FLIP_LEFT_RIGHT
imageEspelhada = imageOriginal.transpose(Image.FLIP_LEFT_RIFHT)
# Mostrar a imagem original
imageOriginal.show

# mostrar a imagem rotacionada
imageEsoelhada.show()
# Salvar a imagem 

img.save('pandaespelhada.jpg')