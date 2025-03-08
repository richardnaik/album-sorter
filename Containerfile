FROM alpine

# install python, pip, and ffmpeg
RUN apk add --update --no-cache python3
RUN apk add --update --no-cache py3-pip
RUN apk add --update --no-cache ffmpeg

# make directories for mounts, not necessary but cleaner
RUN mkdir /app
RUN mkdir /unsorted
RUN mkdir /sorted
