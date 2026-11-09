import DatabaseHandler as dH
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
#region Messages to begin with
root.title("Library")
header = tk.Label(root, text="Library Login")
#endregion

def Root():
        
    header.pack()

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

def create_input_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 3)

    ttk.Label(frame, text='Find what: ').grid(column = 0, row=0, sticky=tk.w)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    ttk.Label(frame, text='Replace with: ').grid(column=0, row=1, sticky=tk.w)
    replacement = ttk.Entry(frame, width=300)
    replacement.grid(column=1, row=0, sticky=tk.w)

    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(frame, text='Match case', variable=match_case, command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    wrap_around = tk.StringV()
    wrap_around_check = ttk.checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()