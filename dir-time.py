#!/usr/bin/python
"""
This utility is uesd for seeing the data and time stamp on files.
It's useful for debugging photo-importer.py program.

Sample output:
$ python dir-time.py *.py
=== file: dir-time.py ===
When created:  Mon Apr  8 20:17:08 2019
Last modified: Thu Apr 11 21:27:06 2019
Last accessed: Fri Apr 12 13:49:33 2019
=== file: photo-import-cli.py ===
When created:  Mon Apr  8 11:17:31 2019
Last modified: Fri Apr 12 13:48:15 2019
Last accessed: Fri Apr 12 13:48:17 2019

"""

import time, sys, os, glob

def show_times(the_file):
    print('=== file: ' + the_file + ' ===')
    print("When created:  %s" % (time.ctime(os.path.getctime(the_file))))
    print("Last modified: %s" % (time.ctime(os.path.getmtime(the_file))))
    print("Last accessed: %s" % (time.ctime(os.path.getatime(the_file))))

if len(sys.argv) < 2:
    for filename in os.listdir(os.getcwd()):
        show_times(filename)
else:
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            proper_files = list()
            the_files = os.listdir(arg)
            for i in the_files:
                proper_files.append(arg + os.path.sep + i)
            for i in proper_files:
                show_times(i)
#            save these for doing subdirectories:
#            for root, dirs, files in os.walk(arg):
#                for filename in files:
#                    show_times(root + os.path.sep + filename)
        else:
            for i in glob.glob(arg):
                show_times(i)
