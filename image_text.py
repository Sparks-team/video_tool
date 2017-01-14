from PIL import Image, ImageDraw
img = Image.new('RGB', (200, 100),"white")
d = ImageDraw.Draw(img)
d.text((20, 20), 'Hello', fill=(255, 0, 0))

img.show()
