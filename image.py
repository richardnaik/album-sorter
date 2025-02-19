import os, sys
import datetime
from PIL import Image
from pillow_heif import register_heif_opener
from PIL import ExifTags
from pprint import pprint

# need to call to be able to rexognize HEIC files
register_heif_opener()

# path to the image or video
imagename = "/home/rick/Pictures/album/20220821_103843.jpg"
#imagename = "/home/rick/Pictures/album/IMG_0771.HEIC"

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exif = image.getexif()
exifdata = exif._get_merged_dict()
timestamp = exifdata[ExifTags.Base.DateTimeOriginal]
orig_create_time = datetime.datetime.fromtimestamp(timestamp)
print(int(object=orig_create_time)) 

image.close()