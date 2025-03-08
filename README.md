Script for sorting and renaming personal photo/video albums. Best run in attached container file.

Command for podman container, assuming the image has been built and named `album-sorter`: 

`podman run -v /path/to/album-sorter:/app -v /path/to/unsorted-media:/unsorted -v /path/to/sorted-media:/sorted --name album-sorter -i -t album-sorter`

Start a bash session in the container, and run:

`pip3 install -r /app/requirements.txt --break-system-packages`

Now you should be able to run `python3 /app/sort.py`, the sorted files will be placed wherever your sorted media directory is.