import tkinter as tk
import os
from tkinter import filedialog

main_window = tk.Tk()
main_window.title(f'{default_name} - Notepad')
window_box = tk.Text()
menu_bar = tk.Menu(main_window)

file_types = (("text files", "*.txt"), ("All files", "*.*"))
def open_file():
	file_path = filedialog.askopenfilename(parent=main_window, title="Open", filetypes=file_types)
	
	if file_path:
		with open(file_path, "r") as file:
			window_box.delete(1.0, tk.END)
			window_box.insert(1.0, file.read())
	
	main_window.title(f'{os.path.basename(file_path)} - Notepad')
	print(file_path)

def save_file():
	file_path = filedialog.asksaveasfilename(parent=main_window, title="Save As")
	
	if file_path:
		with open(file_path, "w") as file:
			file.write(main_window.get(1.0, tk.END))

def close_app():
	main_window.quit()
	
# Menus
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New (Ctrl+N)")
file_menu.add_command(label="New Window (Ctrl+Shift+N)")
file_menu.add_command(label="Open... (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_command(label="Save As... (Ctrl+Shift+S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Page Setup")
file_menu.add_command(label="Print (Ctrl+P)")
file_menu.add_separator()
file_menu.add_command(label="Exit (Ctrl+N)", command=close_app)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo (Ctrl+Z)")
edit_menu.add_command(label="Redo (Ctrl+Y)")
edit_menu.add_separator()
edit_menu.add_command(label="Cut (Ctrl+X)")
edit_menu.add_command(label="Copy (Ctrl+C)")
edit_menu.add_command(label="Paste (Ctrl+P)")
edit_menu.add_command(label="Delete")
edit_menu.add_separator()
edit_menu.add_command(label="Select All (Ctrl+A)")

format_menu = tk.Menu(menu_bar, tearoff=0)
view_menu = tk.Menu(menu_bar, tearoff=0)
help_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Format", menu=format_menu)
menu_bar.add_cascade(label="View", menu=view_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

main_window.config(menu=menu_bar)

window_box.pack()
main_window.mainloop()