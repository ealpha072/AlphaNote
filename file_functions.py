import tkinter as tk
import os
from tkinter import filedialog, messagebox

file_types = (("Text files", "*.txt"), ("All files", "*.*"))
def open_file(editor):
	file_path = filedialog.askopenfilename(title="Open", filetypes=file_types)
	
	if file_path:
		with open(file_path, "r") as file:
			editor.text_area.delete(1.0, tk.END)
			editor.text_area.insert(1.0, file.read())
	
		editor.root.title(f'{file_path} - Notepad')

def save_as_file(editor):
	current_title = editor.root.title()
	default_name="Untitled" if current_title == "Untitled - Notepad" else os.path.basename(current_title.split(" - ")[0])
	
	file_path = filedialog.asksaveasfilename(initialfile=default_name, title="Save As", defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
	
	if file_path:
		with open(file_path, "w") as file:
			file.write(editor.text_area.get(1.0, tk.END))
		
		print(file_path)
		editor.root.title(f'{file_path} - Notepad')

def save_file(editor):
	current_file_path = editor.root.title()
	if os.path.isfile(current_file_path.split(" - ")[0]):
		file_path = current_file_path.split(" - ")[0]
		with open(file_path, "w") as file:
			file.write(editor.text_area.get(1.0, tk.END))
		messagebox.showinfo("Save success", "File saved successfully")
	else:
		save_as_file(editor)
	
def close_app(editor):
	editor.root.quit()