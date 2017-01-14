import PIL
from PIL import ImageDraw, Image, ImageFont
import textwrap
import extract

def get_description_frame(id, t):
	MAX_W, MAX_H = 1280, 720
	img1= Image.new('RGB', (MAX_W, MAX_H), "white")
	draw = ImageDraw.Draw(img1)

	img2 = Image.open(id + "/images/0.jpeg")
	img2 = img2.resize((MAX_W, MAX_H), Image.ANTIALIAS)
	print(img2.size)

	font = ImageFont.truetype('mermaid/Mermaid1001.ttf', 16)
	text = extract.get_story_description()
	astr = t
	para = textwrap.wrap(astr, width=35)
	pad = 10
	current_h =  30
	for line in para:
	    w, h = draw.textsize(line, font=font)
	    draw.text((50, current_h), line, fill="black", font=font)
	    current_h += h + pad
	img = Image.blend(img1, img2, 0.3)
	#img.show()
	img.save(id + "/description.jpeg")
