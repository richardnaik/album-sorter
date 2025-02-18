import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
from pprint import pprint

# need to call to be able to rexognize HEIC files
register_heif_opener()

# path to the image or video
imagename = "/home/rick/Pictures/album/20220821_103843.jpg"
#imagename = "/home/rick/Pictures/album/IMG_0771.HEIC"

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
pprint(TAGS.get('DateTimeOriginal'))
pprint(exifdata.get(TAGS.get('DateTimeOriginal')))  

image.close()