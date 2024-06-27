"""
Rename all the images in the ./images folder. There are images of .jpg, .png
extensions. The images should be renamed to 001_image.jpg(or .png according to 
original extension), 002_image.jpg and so on.
"""
"""
Rename all the images in the ./images folder. There are images of .jpg, .png
extensions. The images should be renamed to 001_image.jpg(or .png according to 
original extension), 002_image.jpg and so on.
"""

import os 

#current working directory 
# print(os. getcwd())

img_path = "./images"

img_list = os.listdir(img_path)

count = 0

for img in img_list:

    count = count +1
    num = str(count).zfill(4)

    name, ext = os.path.splitext(img)
    new_name= f"{num}_dog"+ ext
    source = os.path.join(img_path, img)
    destination = os.path.join(img_path, new_name)

    os.rename(source, destination)