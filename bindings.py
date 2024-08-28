from file_functions import open_file, save_as_file, close_app, save_file
from edit_functions import undo, redo, cut, copy, paste, select_all

def bind_all(editor):
	"""File menu bindings"""
	editor.root.bind("<Control-o>", lambda event: open_file(editor))
	editor.root.bind("<Control-S>", lambda event: save_as_file(editor))
	editor.root.bind("<Control-q>", lambda event: close_app(editor))
	editor.root.bind("<Control-s>", lambda event: save_file(editor))
	
	"""Edit menu bindings (Undo, copy, cut, paste, select all)"""
	editor.root.bind("<Control-z>", lambda event: undo(editor))
	editor.root.bind("<Control-y>", lambda event: redo(editor))
	editor.root.bind("<Control-x>", lambda event: cut(editor))
	editor.root.bind("<Control-c>", lambda event: copy(editor))
	editor.root.bind("<Control-p>", lambda event: paste(editor))
	editor.root.bind("<Control-a>", lambda event: select_all(editor))
	