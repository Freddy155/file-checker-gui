import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        return -1

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_size = get_file_size(file_path)
        update_result_label(file_path, file_size)

def update_result_label(file_path, file_size):
    result_label.config(text=f"File: {file_path}\nSize: {file_size} bytes")

# Create the main window
root = tk.Tk()
root.title("File Size Checker")

# Create and configure the button
select_button = ttk.Button(root, text="Select File", command=open_file_dialog)
select_button.pack()

# Create and configure the result label
result_label = ttk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
