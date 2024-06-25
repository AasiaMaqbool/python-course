from PIL import Image,ImageFilter

img=Image.open('./images/DuaForOlad.png')
filtered_img=img.convert('L')
filtered_img.save("blur.png",'png')
