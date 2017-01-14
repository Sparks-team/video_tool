from PIL import Image, ImageDraw, ImageFont
import textwrap
import extract
import background


def get_title_frame():
	astr = extract.get_story_title()
	para = textwrap.wrap(astr, width=35)

	MAX_W, MAX_H = 1280, 720
	bg = background.get_background()
	im = Image.new('RGB', (MAX_W, MAX_H), bg)
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype(
	    'mermaid/Mermaid1001.ttf', 60)

	current_h, pad = 100, 10
	for line in para:
	    w, h = draw.textsize(line, font=font)
	    draw.text(((MAX_W - w) / 2, current_h), line, fill="black", font=font)
	    current_h += h + pad
	#im.show()
	return im
#im.save('test.png')