# photo-importer
Python tool to import photos into a structured folder archive

This tool will copy only \*.jpg and \*.jpeg files from a given
source directory and put them into a photo archive. My choice
of archive folder is $HOME\Photos

The Photos are arranged in a folder structure of:
$HOME\Photos\(4-digit year)\(2-digit month)\(2-digit date)\(original file name)

just like the Gnome Desktop application Shotwell arranged them.

This script does not delete the files from the source. If a file is already
in the archive, it will not be copied.
