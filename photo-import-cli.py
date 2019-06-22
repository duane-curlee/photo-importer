#!/usr/bin/python
"""
This utility copies photos from a given folder to your home archive.
"""
import shutil
import sys
import os
import datetime

def message(the_str):
    global log_file_node
    log_file_node.write(the_str + '\n')
    print(the_str)

def import_from_to(the_target, the_source):
    for root, dirs, files in os.walk(the_source):
        message('Checking folder: ' + root + os.path.sep)
        for name in files:
            if name[-4:].lower()  == ".jpg" or name[-5:].lower() == ".jpeg":
                source_path_name = root + os.path.sep + name
                the_dt = datetime.datetime.fromtimestamp(os.path.getmtime(source_path_name))
                target_path = the_dt.strftime('%Y') + os.path.sep
                target_path += the_dt.strftime('%m') + os.path.sep
                target_path += the_dt.strftime('%d') + os.path.sep
                target_path = os.path.join(the_target, target_path)
                target_path_name = target_path + name
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                if os.path.exists(target_path_name):
                    message('Not copying, already in archive: ' + source_path_name)
                else:
                    message('Copying %s to: %s' % (source_path_name, target_path_name))
                    shutil.copy2(source_path_name, target_path)
            else:
                message('Not a JPEG file, skipping: %s' % root + os.path.sep + name)

if __name__ == '__main__':
    the_target = os.path.join(os.path.expanduser('~'), 'Photos-testing')
    the_now = datetime.datetime.now()
    the_base_name_ext = os.path.basename(sys.argv[0])
    the_base_name = os.path.splitext(the_base_name_ext)[0]
    log_fname = the_base_name + '-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'

    if not os.path.exists(the_target):
        os.makedirs(the_target)
        log_file_node = open(os.path.join(the_target, log_fname), "w+")
        message(the_base_name_ext + ' started: ' + the_now.strftime('%Y-%m-%d at %H:%M:%S'))
        message('Did not exist, created: ' + the_target)
    else:
        log_file_node = open(os.path.join(the_target, log_fname), "w+")
        message(the_base_name_ext + ' started: ' + the_now.strftime('%Y-%m-%d at %H:%M:%S'))

    if len(sys.argv) < 2:
        import_from_to(the_target, os.getcwd())
    else:
        for arg in sys.argv[1:]:
            if os.path.isdir(arg) == True:
                import_from_to(the_target, arg)
            else:
                message('Not a folder, skipping: ' + arg)

    the_now = datetime.datetime.now()
    message(the_base_name_ext + ' completed: ' + the_now.strftime('%Y-%m-%d at %H:%M:%S'))
    log_file_node.close()
