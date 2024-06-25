from PIL import Image,ImageFilter

img=Image.open('./images/best_image.jpg')
new_image= img.resize((400,200))
new_image.save('thumbnail.jpg')


