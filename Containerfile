FROM ubuntu:24.04

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip ffmpeg

# make directories for mounts, not necessary but cleaner
RUN mkdir /app
RUN mkdir /unsorted
RUN mkdir /sorted
