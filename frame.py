import title_frame
import extract
import os
import title_frame
import PIL
from PIL import Image, ImageDraw, ImageFont
import description_frame
from bs4 import BeautifulSoup
import image_frames
import author_frame
import logo
def get_folder():
	id = extract.get_story_id()
	extra = "https://www.wittyfeed.com/sitemap/"
	if extra in id:
		id = id[id.index(extra) + len(extra):]

	if not os.path.exists(id):
	    os.makedirs(id)

	return id


folder = get_folder()
if not os.path.exists(folder + "/images"):
	os.makedirs(folder + "/images")
if not os.path.exists(folder + "/figcaption"):
	os.makedirs(folder + "/figcaption")
extract.get_images(folder)
img = title_frame.get_title_frame()
img.show()
title_name = get_folder() + "/title_frame.jpeg"
img.save(title_name)

#image frames
id = get_folder()
count = extract.get_images(folder)
image_frames.get_image_frames(count, id)

def get_count():
	return count

#description frame

txt = extract.get_story_description()
clean_text = BeautifulSoup(txt).text
description_frame.get_description_frame(id, clean_text)

#author frame
author_frame.get_author_frame(id)

#logo frame
logo.get_logo_frame(id)









