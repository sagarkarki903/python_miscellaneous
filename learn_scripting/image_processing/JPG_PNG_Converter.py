import sys
import os
from PIL import Image

#grab first and second argument using sys
arg1 = sys.argv[1] #the folder where all the images are
arg2 = sys.argv[2] # the new folder where all the images selected will go

#check if the folder given exists or not. I will use os for this.
if os.path.exists('Converted_PNG'):
    print("File already exists")
else:
    os.makedirs("Converted_PNG")
    print("New Folder Created")

for all_images in os.listdir(arg1):
    if all_images.lower().endswith(".png"):
        png_move = Image.open(all_images)
        png_move.save(f"./{arg2}/{all_images}")
    elif all_images.lower().endswith((".jpg", ".webp")):
        converted = Image.open(all_images)
        converted.save(f"./{arg2}/{all_images}.png")









