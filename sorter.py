import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS

# path to the image or video
imagename = "/home/rick/code/image-sorter/20220821_103843.jpg"

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id).decode("utf-16")
    print(f"{tag:25}: {data}")  