import os
import random
import ctypes

SPI_SETDESKTOPWALLPAPER = 20
SPI_GETDESKWALLPAPER = 115

path = r"C:\Users\theaw\OneDrive\Pictures\wallpapers"
dirList = os.listdir(path)

def filterFolder():
    filteredList = []
    for filename in dirList:
        _, extension = os.path.splitext(filename)
        if extension.lower() in ['.jpg', '.jpeg', '.png']:
            filteredList.append(filename)
    return filteredList


def getImage():
    list = filterFolder()
    rangeInt = len(list)
    ranValue = random.randint(0, rangeInt - 1)
    imageChoice = list[ranValue]
    imagePath = os.path.abspath(os.path.join(path, imageChoice))
    return imagePath

def getCurrentWallpaper():
    buffer = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 512, buffer, 0)
    return buffer.value

def setWallpaper():
    image = getImage()
    current = getCurrentWallpaper()
    while current == image:
        image = getImage()

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, image, 0)

setWallpaper()