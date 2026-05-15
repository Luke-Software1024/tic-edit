import tkinter as tk
from tkinter import ttk, messagebox, filedialog

window = tk.Tk()
window.title("TICEdit Chunk Editor")
window.option_add("*tearOff", 0)

menubar = tk.Menu(window)
window["menu"] = menubar
menu_file = tk.Menu(menubar)
menu_edit = tk.Menu(menubar)
menu_about = tk.Menu(menubar)
menubar.add_cascade(menu=menu_file, label="File")
menubar.add_cascade(menu=menu_edit, label="Edit")
menubar.add_cascade(menu=menu_about, label="About")

menu_file.add_command(label="New")
menu_file.add_command(label="Open...")
menu_file.add_command(label="Save...")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=exit)

menu_edit.add_command(label="New Chunk...")
menu_edit.add_command(label="Open Chunk...")
menu_edit.add_command(label="Save Chunk...")
menu_edit.add_command(label="Delete Chunk")
menu_edit.add_command(label="Replace Chunk...")

menu_about.add_command(label="More info about this chunk type")
menu_about.add_separator()
menu_about.add_command(label="About TICEdit")

window.mainloop()
