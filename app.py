import tkinter as tk
from tkinter import filedialog
from ui_components import create_menu
from bindings import bind_all

class TextEditor:
	def __init__(this, root):
		this.root = root
		this.root.title("Untitled - Notepad")
		this.text_area = tk.Text()
		this.text_area.pack(expand=1, fill="both")
		
		create_menu(this)
		bind_all(this)
	
if __name__ == "__main__":
	root = tk.Tk()
	editor = TextEditor(root)
	root.mainloop()