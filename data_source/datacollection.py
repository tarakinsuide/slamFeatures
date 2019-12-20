import os
from PIL import Image

from google_images_download import google_images_download

resp = google_images_download.googleimagesdownload()

arguments = {"keywords":"airport clocks","limit":200,"print_urls":True, "chromedriver" : "C:\Program Files (x86)\Google\Chrome\chromedriver"}

path = resp.download(arguments)

print(path)