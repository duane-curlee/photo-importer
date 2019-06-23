import tkinter as tk
from tkinter import filedialog
import sys, os, shutil, datetime, tempfile

photo_target = os.path.expanduser('~') + os.path.sep + 'Photos-testing'
photo_source = os.getcwd()

def import_these():
    global photo_source, photo_target
    the_now = datetime.datetime.now()
    the_base_name_ext = os.path.basename(sys.argv[0])
    the_base_name = os.path.splitext(the_base_name_ext)[0]
    log_file_name = the_base_name + '-' + the_now.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    log_file_path = os.path.join(tempfile.gettempdir(), log_file_name)
    log_file_node = open(log_file_path, "w+")

    def message(the_str):
        log_file_node.write(the_str + '\n')
        txt_log.insert(tk.END, the_str + '\n')

    if not os.path.exists(photo_target):
        os.makedirs(photo_target)
        message('Did not exist, created: ' + photo_target)

    message(the_base_name_ext + ' started: ' + the_now.strftime('%Y-%m-%d at %H:%M:%S'))

    for root, dirs, files in os.walk(photo_source):
        message('Checking folder: ' + os.path.normpath(root) + os.path.sep)
        for name in files:
            if name[-4:].lower()  == ".jpg" or name[-5:].lower() == ".jpeg":
                the_source = root + os.path.sep + name
                the_dt = datetime.datetime.fromtimestamp(os.path.getmtime(the_source))
                the_path = the_dt.strftime('%Y') + os.path.sep
                the_path += the_dt.strftime('%m') + os.path.sep
                the_path += the_dt.strftime('%d') + os.path.sep
                the_path = photo_target + os.path.sep + the_path
                the_target = the_path + name
                if not os.path.exists(the_path):
                    os.makedirs(the_path)
                if os.path.exists(the_target):
                    message('Not copying, already in archive: ' + name)
                else:
                    message('Copying %s to: %s' % (name, the_target))
                    shutil.copy2(the_source, the_path)
            else:
                message('Not copying, not a JPEG file: %s' % name)

    message(the_base_name_ext + ' finished: ' + the_now.strftime('%Y-%m-%d at %H:%M:%S'))
    log_file_node.close()
    shutil.copy2(log_file_path, os.path.join(photo_target, log_file_name))

    if os.path.isfile(log_file_path):
        os.remove(log_file_path)

def choose_source():
    global lbl_source, photo_source
    photo_source_orig = photo_source
    photo_source =  filedialog.askdirectory(title = 'Select your source folder', initialdir=os.path.expanduser('~'))
    if len(photo_source) > 0:
        lbl_source.config(text=os.path.normpath(photo_source))
    else:
        photo_source = photo_source_orig
        lbl_source.config(text=os.path.normpath(photo_source))

def choose_target():
    global lbl_target, photo_target
    photo_target_orig = photo_target
    photo_target =  filedialog.askdirectory(title = 'Select your target folder', initialdir=os.path.expanduser('~'))
    if len(photo_target) > 0:
        lbl_target.config(text=os.path.normpath(photo_target))
    else:
        photo_target = photo_target_orig
        lbl_target.config(text=os.path.normpath(photo_target))

root = tk.Tk()
root.title('Photo Importer version 0.3')
root.geometry("800x600")
root.minsize(800, 600)

frame_source = tk.Frame(root)
frame_target = tk.Frame(root)
frame_log = tk.Frame(root)
frame_bottom = tk.Frame(root)

lbl_source_head = tk.Label(frame_source, text="Source: ", width=10)
lbl_target_head = tk.Label(frame_target, text="Target: ", width=10)
lbl_source = tk.Label(frame_source, width=70, text=photo_source, anchor=tk.W, borderwidth=1, relief=tk.GROOVE)
lbl_target = tk.Label(frame_target, width=70, text=photo_target, anchor=tk.W, borderwidth=1, relief=tk.GROOVE)

txt_scrollbar = tk.Scrollbar(frame_log)
txt_log = tk.Text(frame_log, yscrollcommand=txt_scrollbar.set)

btn_choose_source = tk.Button(frame_source, text="Choose source", width=15, command=choose_source)
btn_choose_target = tk.Button(frame_target, text="Choose target", width=15, command=choose_target)
btn_close  = tk.Button(frame_bottom, text="Close",  width = 10, command=root.destroy)
btn_import = tk.Button(frame_bottom, text="Import", width = 10, command=import_these)

frame_source.pack(side=tk.TOP, fill=tk.X, ipadx=10, ipady=5)
lbl_source_head.pack(side=tk.LEFT)
lbl_source.pack(side=tk.LEFT)
btn_choose_source.pack(side=tk.LEFT, padx=5)

frame_target.pack(side=tk.TOP, fill=tk.X, ipadx=10, ipady=5)
lbl_target_head.pack(side=tk.LEFT)
lbl_target.pack(side=tk.LEFT)
btn_choose_target.pack(side=tk.LEFT, padx=5)

frame_log.pack(side=tk.TOP, expand=True, fill=tk.BOTH , padx=5, pady=5)
txt_log.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
txt_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
txt_scrollbar.config(command=txt_log.yview)

frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)
btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_import.pack(side=tk.RIGHT, pady = 10, padx = 10)

root.mainloop()
