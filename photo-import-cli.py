#!/usr/bin/python
"""
This utility copies photos from a given folder to your home archive.
"""
import shutil, sys, os, datetime
photo_home = os.path.expanduser('~') + os.path.sep + 'Photos-testing' + os.path.sep

if len(sys.argv) < 2:
    print('Exiting, a command-line folder name is required.')
else:
    if not os.path.exists(photo_home):
        print('Does not exist, creating: ' + photo_home)
        os.makedirs(photo_home)
    for arg in sys.argv[1:]:
        if os.path.isdir(arg) == True:
            for root, dirs, files in os.walk(arg):
                print("Checking folder: " + root + os.path.sep)
                for name in files:
                    if name[-4:].lower()  == ".jpg" or name[-5:].lower() == ".jpeg":
                        the_source = root + os.path.sep + name
                        the_dt = datetime.datetime.fromtimestamp(os.path.getmtime(the_source))
                        the_path = the_dt.strftime('%Y') + os.path.sep
                        the_path += the_dt.strftime('%m') + os.path.sep
                        the_path += the_dt.strftime('%d') + os.path.sep
                        the_path = photo_home + the_path
                        the_target = the_path + name
                        if not os.path.exists(the_path):
                            os.makedirs(the_path)
                        if os.path.exists(the_target):
                            print('Not copying, already in archive: ' + the_source)
                        else:
                            print('Copying %s to: %s' % (the_source, the_target))
                            shutil.copy2(the_source, the_path)
                    else:
                        print('Not a JPEG file, skipping: %s' % root + os.path.sep + name)
        else:
            print('Not a folder, skipping: ' + arg)
