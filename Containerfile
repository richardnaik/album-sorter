FROM registry.access.redhat.com/ubi9/ubi

# use python 3.11 for consistency
RUN dnf -y install python3.11
RUN python3.11 -m ensurepip --upgrade

# make directories for mounts, not necessary but cleaner
RUN mkdir /app
RUN mkdir /unsorted
RUN mkdir /sorted
