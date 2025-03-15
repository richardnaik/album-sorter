# base libraries
import os
from shutil import copyfile
import json

# image and video libraries
from PIL import Image
from PIL import UnidentifiedImageError
from pillow_heif import register_heif_opener
from PIL.ExifTags import TAGS
from ffmpeg import FFmpeg, FFmpegError

# need to call this to be able to recognize HEIC files
register_heif_opener()

unsorted_dir = '/unsorted'
sorted_dir = '/sorted'

# loop through directory
for file in os.scandir(unsorted_dir):
    full_filename = os.fsdecode(file)
    filename, extension = os.path.splitext(full_filename)

    # initialize these vars as None so the loop knows what to do
    # TODO - shouldn't need to do this
    image = None
    video = None

    # TODO - make this cleaner
    try:
        image = Image.open(full_filename)
    except UnidentifiedImageError as e: # if it's not an image, assume it's as a video
        video = full_filename

    # handle images
    if image is not None: 
        # extract exif data
        exifdata = image.getexif()

        # get the creation date/time from exif data
        original_create_datetime = exifdata.get(306)

        # make sure exif actually has a date/time
        if original_create_datetime is not None:

            # keep the HEIC extension, probably not necessary but it's consistent
            if image.format == 'HEIF':
                extension = 'HEIC'
            else:
                extension = image.format


            # new filename based on original creation date/time
            new_filename = sorted_dir + '/' + original_create_datetime + '.' + extension

            # copy renamed file to sorted dir if it isn't there
            if not os.path.isfile(new_filename):
                print(f"Renaming {full_filename} to {new_filename}")
                copyfile(full_filename, new_filename)
            else:
                print(f"Image {new_filename} already exists")
            

            # reset the image variable
            image = None
        else:
            print(f"{full_filename} does not have a creation date/time in its exif data")

    # handle videos
    elif video is not None:
        # get the file extension so we can use it for the new file
        filename, extension = os.path.splitext(video)
        ffprobe = FFmpeg(executable="ffprobe").input(video, print_format="json", show_streams=None)
        
        try:
            media = json.loads(ffprobe.execute())

            # different video formats have different streams at the 0 index but they should all have the creation time
            original_create_datetime = media['streams'][0]['tags']['creation_time']

            # new filename based on original creation date/time
            new_filename = sorted_dir + '/' + original_create_datetime + extension

            # copy renamed file to sorted dir if it isn't there
            if not os.path.isfile(new_filename):
                print(f"Renaming {video} to {new_filename}")
                copyfile(full_filename, new_filename)
            else:
                print(f"Video {new_filename} already exists")
            
            # reset video variable
            video = None
        except FFmpegError as e:
            print(e.message)
    else: 
        print(f"{full_filename} is an unknown file type")
