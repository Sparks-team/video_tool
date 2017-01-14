import tinify
from PIL import Image
#import compress
tinify.key = "cy_OyREjkxE1klU1gg6Dl3bPiBD4Aj4f"

img = "farhan.jpg"

source = tinify.from_file(img)
# w, h = img
# source.resize()
value = "far.jpg"
source.to_file(value)
f = Image.open(value)
wd, ht = f.size
new_w = 1200
new_h = new_w /(wd/ht)
f.resize((new_w, new_h), Image.ANTIALIAS)
f.save("farhan_resized.jpg")
#compress.compressLoop(value, 5)
