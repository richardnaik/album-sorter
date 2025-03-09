Script for sorting and renaming personal photo/video albums. This is so I can fully sort by original date/time of creation regardless of the image or video format.

Best run in a container with the attached image file, though can also be run natively provided the correct directories are referenced in the code.

Command for a local podman container, assuming the image has been built and named `album-sorter`: 

`podman run -v $HOME/code/unsorted-media:/unsorted -v $HOME/code/sorted-media:/sorted --name album-sorter -i -t album-sorter`

# TODO:
* handle directories, right now it will crash if there is a directory within the unsorted directory
* figure out what to do if the creation date/time doesn't exist in metadata
* make filename format a little cleaner, so things like `00000Z` aren't in there
* auto build container image with github actions or something else