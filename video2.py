#!/usr/bin/env python
import sys
import frame
from cv2 import *

count = frame.get_count()
id = frame.get_folder()
imglist = []
imglist.append(str(id) + "/title_frame.jpeg")
imglist.append(str(id) + "/description.jpeg")
for i in range(1, count):
	imglist.append(str(id) + "/" + str(i) + ".jpeg")

imglist.append(str(id) + "/author.jpeg")
imglist.append(str(id) + "/logo.png")
# im2 = cv.LoadImage("2.jpeg")

# if not im1:
#     print "Error loading image"
img = []
for x in range(0, len(imglist)):
	print(imglist[x])
	img.append(cv.LoadImage(imglist[x]))

fps = 1
waitKey(10)
frame_size = cv.GetSize(img[0])

writer = cv.CreateVideoWriter(id + "/" + id + "output.avi", cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, frame_size, True)

if not writer:
    print "Error in creating video writer"
    sys.exit(1)
else:
	#print(len(img))
	for k in range(0, len(img)):
		cv.WriteFrame(writer, img[k])
    # cv.WriteFrame(writer, im1)
    # cv.WriteFrame(writer, im2)

del writer