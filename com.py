from __future__ import division
import os
from PIL import Image



def compressLoop(infile):
	 baseName, e = os.path.splitext(infile)

	 f, e = os.path.splitext(infile)
	 f = baseName + str(1)
	 outfile = f + ".jpg"
	 compImg = Image.open(infile)
	 wd, ht = compImg.size
	 if wd is >1280
		 new_w = 1200
	elif wd in range(1024, 1281):
		new_w = 800
	elif wd in range(800, 1024):
		new_w = 800
	else:
		new_w = 500
	 new_h = new_w /(wd/ht)
	 compImg.thumbnail((int(new_w), int(new_h)), Image.ANTIALIAS)
	 compImg.save(outfile, "JPEG", quality=90)

compressLoop("k.jpg")