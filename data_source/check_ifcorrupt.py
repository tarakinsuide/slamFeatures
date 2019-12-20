import cv2
import numpy as np
import os
from PIL import Image

path = r'C:\Users\Admin\PycharmProjects\SlamFeatures\downloads'

def checkcorrupt(filename):
    for images in os.listdir(path + '\\' + filename):
        try:
            with Image.open(path + "\\" + filename + "\\" + images) as im:
                print('ok')
        except:
            print(path + "\\" + filename)
            os.remove(path + "\\" + filename + "\\" + images)

for files in os.listdir(path):
    checkcorrupt(files)