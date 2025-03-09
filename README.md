Script for sorting and renaming personal photo/video albums. Best run in attached container file.

Command for podman container, assuming the image has been built and named `album-sorter`: 

`podman run -v $HOME/code/album-sorter:/app -v $HOME/code/unsorted-media:/unsorted -v $HOME/code/sorted-media:/sorted --name album-sorter -i -t album-sorter`

Now you should be able to run `python /app/sort.py` from inside the container the sorted files will be placed wherever your sorted media directory is.