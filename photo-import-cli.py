#!/usr/bin/python
"""
This utility copies photos from a given folder to your home archive.
"""
import shutil, sys, os, datetime
photo_home = os.path.join(os.path.expanduser('~'), 'Photos-testing')
the_now = datetime.datetime.now()
the_base_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
log_fname = the_base_name + '-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'

def message(the_str):
    global log_file_node
    log_file_node.write(the_str + '\n')
    print(the_str)

def import_these(the_folder):
    global photo_home
    for root, dirs, files in os.walk(the_folder):
        message('Checking folder: ' + root + os.path.sep)
        for name in files:
            if name[-4:].lower()  == ".jpg" or name[-5:].lower() == ".jpeg":
                the_source = root + os.path.sep + name
                the_dt = datetime.datetime.fromtimestamp(os.path.getmtime(the_source))
                the_path = the_dt.strftime('%Y') + os.path.sep
                the_path += the_dt.strftime('%m') + os.path.sep
                the_path += the_dt.strftime('%d') + os.path.sep
                the_path = os.path.join(photo_home, the_path)
                the_target = the_path + name
                if not os.path.exists(the_path):
                    os.makedirs(the_path)
                if os.path.exists(the_target):
                    message('Not copying, already in archive: ' + the_source)
                else:
                    message('Copying %s to: %s' % (the_source, the_target))
                    shutil.copy2(the_source, the_path)
            else:
                message('Not a JPEG file, skipping: %s' % root + os.path.sep + name)

if not os.path.exists(photo_home):
    os.makedirs(photo_home)
    log_file_node = open(os.path.join(photo_home, log_fname), "w+")
    message(the_base_name + ' started: ' + the_now.strftime('%Y-%m-%d %H-%M-%S'))
    message('Did not exist, created: ' + photo_home)
else:
    log_file_node = open(os.path.join(photo_home, log_fname), "w+")
    message(the_base_name + 'started: ' + the_now.strftime('%Y-%m-%d %H-%M-%S'))

if len(sys.argv) < 2:
    import_these(os.getcwd())
else:
    for arg in sys.argv[1:]:
        if os.path.isdir(arg) == True:
            import_these(arg)
        else:
            message('Not a folder, skipping: ' + arg)

the_now = datetime.datetime.now()
message(the_base_name + ' completed: ' + the_now.strftime('%Y-%m-%d %H-%M-%S'))
log_file_node.close()
