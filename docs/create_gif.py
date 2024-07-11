#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import glob
import os

SCRIPT_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR_ABS_PATH, 'slides.gif')

images = [Image.open(img)
          for img in glob.glob(f'{SCRIPT_DIR_ABS_PATH}/image*.png')]

font = ImageFont.truetype("arial.ttf", 40)

for i, img in enumerate(images):
    draw = ImageDraw.Draw(img)
    text = f"{i+1}"
    position = (10, 10)
    draw.text(position, text, fill="white", font=font)
    images[i] = img

images[0].save(OUTPUT_FILE, save_all=True,
               append_images=images[1:], duration=2000, loop=0)
