import os, sys
import ffmpeg
from pprint import pprint

pprint(ffmpeg.probe("IMG_0111.MOV")["streams"])