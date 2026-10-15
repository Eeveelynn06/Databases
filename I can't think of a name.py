import DatabaseHandler as dH
import tkinter as tk

def Root():
    root = tk.Tk()
    root.title("Library")
    header = tk.Label(root, text="Library")
    header.pack()

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

Root()