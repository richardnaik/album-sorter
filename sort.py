import os, sys
from PIL import Image
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
import ffmpeg
from pprint import pprint

# need to call to be able to rexognize HEIC files
register_heif_opener()

# dir with unsorted media
unsorted_dirname = "C:/Users/richa/code/unsorted-media"
unsorted_dir = os.fsencode(unsorted_dirname)

# loop through directory
for file in os.listdir(unsorted_dir):
    filename = os.fsdecode(file)
    # handle images
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".heic") or filename.lower().endswith(".png"): 
        image = Image.open(unsorted_dirname + '/' + filename)

        # extract EXIF data
        exifdata = image.getexif()

        # get the creation date/time from exif data
        original_create_datetime = exifdata.get(306)

        # TODO copy file to sorted dir based on exif date
        print(f"Renaming {filename} to {original_create_datetime}")
    # handle videos
    elif filename.lower().endswith(".mp4") or filename.lower().endswith(".mov"):
        print(filename)
        # TODO get right info from ffmpeg probe
        #pprint(ffmpeg.probe("IMG_0111.MOV")["streams"])
