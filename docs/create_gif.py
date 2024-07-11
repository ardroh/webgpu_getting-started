#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import glob
import os
import json

SCRIPT_DIR_ABS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR_ABS_PATH, 'slides.gif')

images = [Image.open(img)
          for img in glob.glob(f'{SCRIPT_DIR_ABS_PATH}/image*.png')]

font = ImageFont.truetype("arial.ttf", 15)
footer_font = ImageFont.truetype("arial.ttf", 10)

metadata_file_path = os.path.join(SCRIPT_DIR_ABS_PATH, 'metadata.json')
images_metadata = {}
if os.path.exists(metadata_file_path):
    with open(metadata_file_path, 'r') as f:
        metadata = json.load(f)
        images_metadata = metadata.get('images', {})

for i, img in enumerate(images):
    draw = ImageDraw.Draw(img)
    filename = f'image{i+1}.png'
    metadata = next(
        (m for m in images_metadata if m['filename'] == filename), None)
    text = f"{i+1}: {metadata['description']}" if metadata else f"{i+1}"
    draw.rectangle([(10, 10), (20 + draw.textlength(text, font=font),
                   20 + font.getbbox(text)[3])], fill="black")
    draw.text((15, 15), text, fill="white", font=font)
    footer_text = 'ardroh/webgpu_getting-started.git'
    img_width, img_height = img.size
    footer_len = draw.textlength(footer_text, font=footer_font)
    draw.text((img_width - footer_len - 20, img_height - 30),
              footer_text, fill="white", font=footer_font)
    images[i] = img

images[0].save(OUTPUT_FILE, save_all=True,
               append_images=images[1:], duration=2000, loop=0)
