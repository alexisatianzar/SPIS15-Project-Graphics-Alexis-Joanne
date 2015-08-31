
#ffmpeg -i IMG_3274.MOV -r 1 -s 200x400 -f image2 foo-%03d.jpeg

from PIL import Image, ImageDraw

#Joanne7 = Image.open("/home/linux/ieng6/spis15/spis15ab/Downloads/foo-007.jpeg")

def rotateIm(im, number):
    
    image = im.rotate(90)
    image.save("Joanne" + str(number).zfill(3)+ ".png")
    image.show()
    
import imghdr
import os


def changeFolderPics(folder):
    number = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            newPic = Image.open(file_path)
            rotateIm(newPic, number)
            number = number + 1

def cutJoanneMouth(folder):
    number = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            framePic = Image.open(file_path)
            mouthCut = Image.new('RGB', pic.size, (0, 0, 0))
            for x in range (150, 170):
                for y in range(250,284):
                    (mouthR, mouthG, mouthB) = framePic.getpixel((x,y))
                    mouthCut.putpixel((x,y), (mouthR, mouthG, mouthB))
                    mouthCut.show()
            number = number + 1


def cutJoanne(folder):
##    number = 0
##    for dirpath, dirnames, filenames in os.walk(folder):
##        for filename in filenames:
##            file_path = os.path.join(dirpath, filename)
##            framePic = Image.open(file_path)
            mouthCut = Image.new('RGB', folder.size, (0, 0, 0))
            for x in range (150, 170):
                for y in range(250,284):
                    (mouthR, mouthG, mouthB) = folder.getpixel((x,y))
                    mouthCut.putpixel((x,y), (mouthR, mouthG, mouthB))
                    mouthCut.show()
##            number = number + 1
