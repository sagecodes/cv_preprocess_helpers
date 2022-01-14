#%% Command example: python resize.py -d /geese_small_val -s 800 600
from PIL import Image
import os
import argparse

#%%
def rescale_images(directory, output_folder, size):

    for img in os.listdir(directory):
        if os.path.isdir(directory+img):
            continue
        im = Image.open(directory+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(output_folder+img)

        width, height = im.size
        print(width)
        print(height)

#%%

input_img_folder = '../datasets/signs_resize/'

os.makedirs(input_img_folder+"/resized/", exist_ok=True)

output_folder = input_img_folder+'resized/'
#%%
rescale_images(input_img_folder, output_folder, (800,600))

# %%
