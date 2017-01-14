import PIL
from PIL import ImageDraw, Image, ImageFont
import textwrap


MAX_W, MAX_H = 640, 480
img1= Image.new('RGB', (MAX_W, MAX_H), "white")
draw = ImageDraw.Draw(img1)

img2 = Image.open("house.jpg")
img2 = img2.resize((MAX_W, MAX_H), Image.ANTIALIAS)
print(img2.size)


font = ImageFont.truetype('comfortaa/Comfortaa-Bold.ttf', 14)
astr = '''This is a sample text of no use. This is a sample text of no use.2 This is a sample text of no use. This is a sample text of no use.2 This is a sample text of no use. This is a sample text of no use.2 This is a sample text of no use. This is a sample text of no use.2 This is a sample text of no use. This is a sample text of no use.2 This is a sample text of no use. This is a sample text of no use.2'''
para = textwrap.wrap(astr, width=35)
pad = 10
current_h =  30
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text((50, current_h), line, fill="black", font=font)
    current_h += h + pad
Image.blend(img1, img2, 0.5).show()
