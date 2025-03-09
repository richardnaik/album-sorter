FROM alpine

LABEL org.opencontainers.image.source=https://github.com/richardnaik/album-sorter
LABEL org.opencontainers.image.description="album-sorter"
LABEL org.opencontainers.image.licenses=MIT

# install python, pip, and ffmpeg
RUN apk add --update --no-cache python3
RUN apk add --update --no-cache py3-pip
RUN apk add --update --no-cache ffmpeg

# install python libs, using the break system packages flag to let pip3 install them.
# for some reason anything that pip installs is in conflict with the system packages
RUN pip3 install pillow --break-system-packages
RUN pip3 install pillow_heif --break-system-packages
RUN pip3 install python-ffmpeg --break-system-packages

# make directories for mounts, not necessary but cleaner
RUN mkdir /app
RUN mkdir /unsorted
RUN mkdir /sorted
