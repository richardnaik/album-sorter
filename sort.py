import os
from shutil import copyfile
import configparser
from pprint import pprint
from PIL import Image
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
import ffmpeg

# need to call to be able to recognize HEIC files
register_heif_opener()

config = configparser.RawConfigParser() 
config.read_file(open(r"./config.cfg")) 

# directory with unsorted media
unsorted_dirname = config.get('directories', 'unsorted')
unsorted_dir = os.fsencode(unsorted_dirname)

# directory for sorted media
sorted_dirname = config.get('directories', 'sorted')

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
        new_filename = sorted_dirname + "\\" + original_create_datetime + extension
        print(new_filename)

        # copy file to sorted dir with new name based on exif date
        print(f"Renaming {full_filename} to {new_filename}")
        copyfile(full_filename, new_filename)

    # handle videos
    elif filename.lower().endswith(".mp4") or filename.lower().endswith(".mov"):
        print(filename)
        # TODO get right info from ffmpeg probe
        #pprint(ffmpeg.probe("IMG_0111.MOV")["streams"])
