import os
import shutil
from pprint import pprint
from PIL import Image
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
import ffmpeg

# need to call to be able to recognize HEIC files
register_heif_opener()

# directory with unsorted media
unsorted_dirname = "/home/rick/code/unsorted-media"
unsorted_dir = os.fsencode(unsorted_dirname)

# directory for sorted media
sorted_dirname = "/home/rick/code/sorted-media"

# loop through directory
for file in os.scandir(unsorted_dir):
    full_filename = os.fsdecode(file)
    filename, extension = os.path.splitext(full_filename)

    # handle images
    if extension.lower() == ".jpg" or extension.lower() == ".heic" or extension.lower() == ".png": 
        image = Image.open(full_filename)
        #print(image.format)

        # extract exif data
        exifdata = image.getexif()

        # TODO handle files with no exif date or no extension
        # get the creation date/time from exif data
        original_create_datetime = exifdata.get(306)

        # copy file to sorted dir with new name based on exif date
        print(f"Renaming {full_filename} to {original_create_datetime}{extension}")
        shutil.copyfile(full_filename, sorted_dirname + '/' + original_create_datetime + extension)

    # handle videos
    elif filename.lower().endswith(".mp4") or filename.lower().endswith(".mov"):
        print(filename)
        # TODO get right info from ffmpeg probe
        #pprint(ffmpeg.probe("IMG_0111.MOV")["streams"])
