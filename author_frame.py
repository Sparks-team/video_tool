import PIL
import extract
from PIL import ImageDraw, Image, ImageFont
import textwrap
import background

def get_author_frame(id):
	astr = extract.get_author()
	text = "Story By - " + astr
	para = textwrap.wrap(text, width=10)
	MAX_W, MAX_H = 1280, 720
	bg = background.get_background()
	im = Image.new('RGB', (MAX_W, MAX_H), bg)
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype('type_keys/TypeKeysFilled.ttf', 50)

	current_h, pad = 100, 10
	for line in para:
	    w, h = draw.textsize(line, font=font)
	    draw.text(((MAX_W - w) / 2, current_h), line, fill="black", font=font)
	    current_h += h + pad
	im.show()
	print(text)
	im.save(id + "/author.jpeg")