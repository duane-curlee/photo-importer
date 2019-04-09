#!/usr/bin/python

import shutil, sys, os, datetime
photo_home = os.path.expanduser('~') + os.path.sep + 'Photos-testing' + os.path.sep
if not os.path.exists(photo_home):
    os.makedirs(photo_home)

if len(sys.argv) < 2:
    print('Exiting, a command-line folder name is required.')
else:
    for arg in sys.argv[1:]:
        if os.path.isdir(arg) == True:
            for root, dirs, files in os.walk(arg):
                print("Checking folder: " + root + os.path.sep)
                for name in files:
                    if name[-4:].lower()  == ".jpg" or name[-5:].lower() == ".jpeg":
#                        print("%s last modified: %s" % (name, time.ctime(os.path.getmtime(root + os.path.sep + name))))
#                        print("%s created: %s"       % (name, time.ctime(os.path.getctime(root + os.path.sep + name))))
                        the_dt = datetime.datetime.fromtimestamp(os.path.getmtime(root + os.path.sep + name))
                        the_path = the_dt.strftime('%Y') + os.path.sep
                        the_path += the_dt.strftime('%m') + os.path.sep
                        the_path += the_dt.strftime('%d') + os.path.sep
                        the_path = photo_home + the_path
                        if not os.path.exists(the_path):
                            os.makedirs(the_path)
                        print('Copying %s to: %s' % (root + os.path.sep + name, the_path + name))
                        shutil.copy2(root + os.path.sep + name, the_path)
                    else:
                        print('Not a JPEG file, skipping: %s' % name)
        else:
            print('Not a folder, skipping: ' + arg)
