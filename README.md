Script for sorting and renaming personal photo/video albums. Best run in attached container file.

Command for podman container, assuming the image has been built and named `album-sorter`: 

`podman run -v $HOME/code/unsorted-media:/unsorted -v $HOME/code/sorted-media:/sorted --name album-sorter -i -t album-sorter`