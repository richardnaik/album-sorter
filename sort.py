# base libraries
import os
from shutil import copyfile
import configparser
import json

# image and video libraries
from pprint import pprint
from PIL import Image
from PIL import UnidentifiedImageError
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
from ffmpeg import FFmpeg, FFmpegError

# need to call this to be able to recognize HEIC files
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

    try:
        image = Image.open(full_filename)
    except UnidentifiedImageError as e: # if it's not image, try to open it as a video
        video = full_filename

    # handle images
    if image is not None: 
        # extract exif data
        exifdata = image.getexif()

        # get the creation date/time from exif data
        original_create_datetime = exifdata.get(306)

        # make sure exif actually has a date/time
        if original_create_datetime is not None:
            # new filename based on original creation date/time
            new_filename = sorted_dirname + "/" + original_create_datetime + "." + image.format

            # copy file to sorted dir
            print(f"Renaming {full_filename} to {new_filename}")
            copyfile(full_filename, new_filename)

            # reset the image variable
            image = None

    # handle videos
    elif video is not None:
        print(video)
        
        ffprobe = FFmpeg(executable="ffprobe").input(video, print_format="json", show_streams=None)
        
        try:
            media = json.loads(ffprobe.execute())
            print(media['streams'][0]['tags']['creation_time'])
            video = None
        except FFmpegError as e:
            print(e.message)
    else: 
        print(f"{full_filename} is an unknown file type")
