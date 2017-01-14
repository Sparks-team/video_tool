import PIL
import textwrap
from PIL import Image, ImageFont, ImageDraw

#font = ImageFont.load("arial.pil")
text = "11 Most Embarrassing Photos Ever Spotted On The Internet"
para = textwrap.wrap(text, width=15)
max_width, max_height =	(640, 480)
draw = ImageDraw.Draw(img)
img = Image.new("RGB", (width,height),"white")
font = ImageFont.truetype("comfortaa/Comfortaa-Bold.ttf", 40)

#textWidth, textHeight = draw.textsize(text, font=font)


# current = (height - textHeight)/2
# for line in para:
# 	draw.text(((width - textWidth)/2, current), line,fill = "black", font=font)
# 	draw = ImageDraw.Draw(img)
# 	current = current + 50

current_h, pad = 50, 10
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((width - w) / 2, current_h), line, font=font)
    current_h += h + pad

img.show()