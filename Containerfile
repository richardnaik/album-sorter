FROM registry.access.redhat.com/ubi9/ubi

# use python 3.11 for consistency
RUN dnf -y install python3.11
RUN python3.11 -m ensurepip --upgrade

# make directories for mounts, not necessary but cleaner
RUN mkdir /app
RUN mkdir /unsorted
RUN mkdir /sorted

# get the required python libs, reqs file needs to be in the same directory you're building from
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt