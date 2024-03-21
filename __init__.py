"""
The script adds the shortcut to the text editor to delete the current line, just like in VS Code.
CTRL + SHIFT + BACKSPACE by default.
This program is free to use,
feel free to change and redistribute anything from this program (under the License).
The code is short and simple using only the Blender Python api.
"""

bl_info = {
    "name": "Text editor shortcut: Delete Line",
    "author": "Matej Zeman <matej.zeman01@gmail.com>",
    "version": (1, 2),
    "blender": (4, 2, 0),
    "category": "shortcut",
    "location": "text editor",
    "description": "Adds shortcut (CTRL + SHIFT + BACKSPACE) to delete current line in text editor\
(behaves like in VS Code).",
}

try:
    if "bpy" in locals():
        import importlib
        importlib.reload(text_ot_delete_line)
    else:
        from . import text_ot_delete_line
    import bpy
except ImportError as exp:
    raise ImportError(
        "<<< Probably missing bpy module >>>\n\
             Hint: place the folder inside Blender's addons folder. Or use preferences to install."
    ) from exp

classes = [
    text_ot_delete_line.TEXT_OT_DeleteLine,
]

def register():
    """ Registers the operator and adds the shortcut to the text editor. """
    for cl in classes:
        bpy.utils.register_class(cl)
    text_ot_delete_line.TEXT_OT_DeleteLine.create_shortcut()

def unregister():
    """ Unregisters the operator and removes the shortcut from the text editor. """
    text_ot_delete_line.TEXT_OT_DeleteLine.remove_shortcut()
    for cl in reversed(classes):
        bpy.utils.unregister_class(cl)
