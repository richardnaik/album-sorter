Script for sorting and renaming personal photo/video albums.

Create command for podman container: podman create -v $HOME/code/album-sorter:/app -v $HOME/code/unsorted-media:/unsorted -v $HOME/code/sorted-media:/sorted -i -t album-sorter