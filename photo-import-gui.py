import tkinter as tk
from tkinter import filedialog
import os, datetime

photo_target = os.path.expanduser('~') + os.path.sep + 'Photos-testing'
photo_source = os.getcwd()

root = tk.Tk()
root.title('Photo Importer version 0.1')
root.geometry("800x600")
root.minsize(800, 600)

def import_them():
    print("Importing. Naw, we're still testing.")

def choose_source():
    global lbl_source
    folder_name =  filedialog.askdirectory(title = 'Select your source folder', initialdir=os.path.expanduser('~'))
    if len(folder_name) > 0:
        lbl_source.config(text=os.path.normpath(folder_name))

def choose_target():
    global lbl_target
    folder_name =  filedialog.askdirectory(title = 'Select your target folder', initialdir=os.path.expanduser('~'))
    if len(folder_name) > 0:
        lbl_target.config(text=os.path.normpath(folder_name))

frame_source = tk.Frame(root)
frame_target = tk.Frame(root)
frame_log = tk.Frame(root)
frame_bottom = tk.Frame(root)

lbl_source_head = tk.Label(frame_source, text="Source: ", width=10)
lbl_target_head = tk.Label(frame_target, text="Target: ", width=10)
lbl_source = tk.Label(frame_source, width=70, text=photo_source, anchor=tk.W, borderwidth=1, relief=tk.GROOVE)
lbl_target = tk.Label(frame_target, width=70, text=photo_target, anchor=tk.W, borderwidth=1, relief=tk.GROOVE)

txt_log = tk.Text(frame_log)

btn_choose_source = tk.Button(frame_source, text="Choose source", width=15, command=choose_source)
btn_choose_target = tk.Button(frame_target, text="Choose target", width=15, command=choose_target)
btn_close  = tk.Button(frame_bottom, text="Close",  width = 10, command=root.destroy)
btn_import = tk.Button(frame_bottom, text="Import", width = 10, command=import_them)

frame_source.pack(side=tk.TOP, fill=tk.X, ipadx=10, ipady=5)
lbl_source_head.pack(side=tk.LEFT)
lbl_source.pack(side=tk.LEFT)
btn_choose_source.pack(side=tk.LEFT, padx=5)

frame_target.pack(side=tk.TOP, fill=tk.X, ipadx=10, ipady=5)
lbl_target_head.pack(side=tk.LEFT)
lbl_target.pack(side=tk.LEFT)
btn_choose_target.pack(side=tk.LEFT, padx=5)

frame_log.pack(side=tk.TOP, expand=True, fill='both', padx=5, pady=5)
txt_log.pack(side=tk.TOP, expand=True, fill='both')

frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)
btn_close.pack(side=tk.RIGHT, pady = 10, padx = 10)
btn_import.pack(side=tk.RIGHT, pady = 10, padx = 10)

root.mainloop()
