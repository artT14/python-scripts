####
# 1. Takes a folder of png's, finds the average rgb color
# 2. Find the complementary color of the average
# 3. Fills the background with the complementary color
# 4. Places Image on Top
# ###
import os
from PIL import Image, ImageDraw
import numpy as np

def get_average_color(image):
    np_image = np.array(image)
    r, g, b, a = np_image[:,:,0], np_image[:,:,1], np_image[:,:,2], np_image[:,:,3]
    
    mask = a > 0
    avg_r = np.mean(r[mask])
    avg_g = np.mean(g[mask])
    avg_b = np.mean(b[mask])

    return int(avg_r), int(avg_g), int(avg_b)

def get_complementary_color(color):
    r, g, b = color
    comp_r = 255 - r
    comp_g = 255 - g
    comp_b = 255 - b
    return (comp_r, comp_g, comp_b)

def add_complementary_background(image_path):
    image = Image.open(image_path).convert("RGBA")

    avg_color = get_average_color(image)
    complementary_color = get_complementary_color(avg_color)

    new_image = Image.new("RGBA", image.size, complementary_color)
    new_image.paste(image, (0, 0), image)
    
    new_image_path = "complementary_" + os.path.basename(image_path)
    new_image.save(new_image_path)

current_directory = os.getcwd()
all_files = os.listdir(current_directory)

for file_name in all_files:
    # Skip directories
    if os.path.isdir(file_name) or ".png" not in file_name:
        continue
    try:
        add_complementary_background(file_name)
    except Exception as e:
        print(f"Could not perform operation on {file_name}. Error: {e}")