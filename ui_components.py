import tkinter as tk
from file_functions import open_file, save_as_file, close_app, save_file
from edit_functions import undo, redo, cut, copy, paste

def create_menu(editor):
	menu_bar = tk.Menu(editor.root)
	# File menu
	file_menu = tk.Menu(menu_bar, tearoff=0)
	file_menu.add_command(label="New (Ctrl+N)")
	file_menu.add_command(label="New Window (Ctrl+Shift+N)")
	file_menu.add_command(label="Open... (Ctrl+O)", command=lambda: open_file(editor))
	file_menu.add_command(label="Save (Ctrl+S)", command=lambda: save_file(editor))
	file_menu.add_command(label="Save As... (Ctrl+Shift+S)", command=lambda: save_as_file(editor))
	file_menu.add_separator()
	file_menu.add_command(label="Page Setup")
	file_menu.add_command(label="Print (Ctrl+P)")
	file_menu.add_separator()
	file_menu.add_command(label="Exit (Ctrl+Q)", command=lambda: close_app(editor))
	
	# Edit menu
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
	
	editor.root.config(menu=menu_bar)