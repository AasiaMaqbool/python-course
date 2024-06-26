import sys
import os
from PIL import Image


image_Folder=sys.argv[1]
output_Folder=sys.argv[2]

if not os.path.exists(output_Folder):
    os.makedirs(output_Folder)

for filename in os.listdir(image_Folder):
    img=Image.open(f'{image_Folder}{filename}')
    Image.save(f'{output_Folder}{filename}.png','png')
    print('all done!')