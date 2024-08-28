import tkinter as tk

def undo(editor):
	editor.text_area.edit_undo()
	
def redo(editor):
	editor.text_area.edit_redo()
	
def cut(editor):
	editor.text_area.event_generate("<<Cut>>")
	
def copy(editor):
	editor.text_area.event_generate("<<Copy>>")

def paste(editor):
	editor.text_area.event_generate("<<Paste>>")
	
def select_all(editor):
	#editor.text_area.event_generate("<<SelectAll>>")
	editor.text_area.tag_add("select", "1.0", "end")
	#editor.text_area.tag_config("select", background="blue")
	return "break"