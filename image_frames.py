from __future__ import division
import PIL
from PIL import ImageDraw, Image, ImageFont
import textwrap
import glob
import 	os
import background
def get_ext_image(path):
    filename, file_extension = os.path.splitext(path)
    return file_extension

def get_image_frames(count, id):
	for x in range(1, count):
		#3font = ImageFont.truetype("", 40)
		
		filename = glob.glob(os.path.join(id + "/images/" +  str(x) + '.*'))
		print(filename)
		#print(filename[x])
		img = Image.open(filename[0])
		size = wd, ht = img.size
		#print(str(w) + " " + str(h))
		# print wd, ht
		# aspect_ratio = float(wd/ht)
		# print(aspect_ratio)
		new_w = 550
		new_h = new_w /(wd/ht)
		print(new_h)
		img = img.resize((int(new_w), int(new_h)), Image.ANTIALIAS)
		#img.show()
		image_pad_h = 10
		#creating background
		draw = ImageDraw.Draw(img)
		MAX_W, MAX_H = 1280, 720
		bg = background.get_background()
		im = Image.new('RGB', (MAX_W, MAX_H), bg)
		draw = ImageDraw.Draw(im)
		im.paste(img,(45,image_pad_h))
		#im.show()
		font = ImageFont.truetype('mermaid/Mermaid1001.ttf', 20)
		f = open(id + "/figcaption/" + str(x) + ".txt")
		text = f.read()
		astr = text.encode('utf-8')
		para = textwrap.wrap(astr, width=50)
		pad = 10
		current_h = new_h + image_pad_h + 5
		for line in para:
		    w, h = draw.textsize(line, font=font)
		    draw.text(((MAX_W - w) / 2, current_h), line, fill="black", font=font)
		    current_h += h + pad
		#im.show()
		im.save(id + "/" + str(x) + ".jpeg")
		


