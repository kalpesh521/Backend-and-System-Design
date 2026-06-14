from text_editor import TextEditor
from history import History

text_editor = TextEditor()
history = History()

history.save_state(text_editor.save())

text_editor.write("Hello, World!")
history.save_state(text_editor.save())

text_editor.write(" Good")
history.save_state(text_editor.save())

print("Current:", text_editor.get_text())

text_editor.restore(history.undo())
print("After undo:", text_editor.get_text())

text_editor.restore(history.redo())
print("After redo:", text_editor.get_text())
