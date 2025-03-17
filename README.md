Script for sorting and renaming personal photo/video albums by original date/time of creation regardless of the image/video format and naming scheme.

Best run in a container with the attached image file, though can also be run natively provided the correct directories are referenced in the code.

Example command for running it in a podman container: 

`podman run -v /mnt/archive/archive/ray/ray:/unsorted -v /mnt/archive/archive/ray_sorted:/sorted --entrypoint python ghcr.io/richardnaik/album-sorter:latest /app/sort.py > /var/log/album-sorter`

# TODO:
* handle directories, right now it will crash if there is a directory within the unsorted directory
* figure out what to do if the creation date/time doesn't exist in metadata
* make filename format a little cleaner, so things like `00000Z` aren't in there
