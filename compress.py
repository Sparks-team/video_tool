from __future__ import division
import os
from PIL import Image


def compressLoop(infile, times):

    n = 1
    baseName, e = os.path.splitext(infile)
    # wd, ht = infile.size
    # new_w = 1200
    # new_h = new_w /(wd/ht)
    #infile.resize(new_w, new_h, Image.ANTIALIAS)
    x = 100
    while n <= times:
        f, e = os.path.splitext(infile)
        f = (baseName + str(n))
        outfile = f + ".jpg"
            #open previously generated file
        compImg = Image.open(infile)
            #compress file at 50% of previous quality
        x = x/2
        print(x)
        wd, ht = compImg.size
        new_w = 1200
        new_h = new_w /(wd/ht)
        print(new_w, new_h)
        compImg.resize((int(new_w), int(new_h)), Image.ANTIALIAS)
        compImg.show()
        compImg.save(outfile, "JPEG", quality=int(x))
        #f.resize((int(new_w), int(new_h)), Image.ANTIALIAS)
        infile = outfile
        n = n+1

    
# def further_com(newname):
#      n = 1
#     baseName, e = os.path.splitext(newname)
#     x = 100
#     while n <= 5:
#         f, e = os.path.splitext(newname)
#         f = (str(n) + baseName)
#         outfile = f + ".jpg"
#             #open previously generated file
#         compImg = Image.open(newname)
#             #compress file at 50% of previous quality
#         print("further compress")
#         x = x/2
#         print(x) 
#         #compImg.save(outfile, "JPEG", quality=int(x))
#         newname = outfile
#         n = n+1

def main():
     infile = "farhan.jpeg"
     times = 6
     compressLoop(infile, times)
     # in = times + infile
     # further_com(in)

main()