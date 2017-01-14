from __future__ import division
import os
from PIL import Image

f = Image.open("house.jpg")
wd, ht = f.size
new_w = 600
new_h = new_w /(wd/ht)
f.thumbnail((int(new_w), int(new_h)), Image.ANTIALIAS)
f.save("house_recreated.jpg", "JPEG", quality=50)