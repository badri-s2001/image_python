import sys
import os
from PIL import Image

src_folder = sys.argv[1]
dest_folder = sys.argv[2]


if(not os.path.exists(dest_folder)):
    os.makedirs(dest_folder)

for filename in os.listdir(src_folder):
    img = Image.open(f"{src_folder}\{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{dest_folder}\{clean_name}.png', 'png')
