""" The script adds the shortcut to the text editor to delete the current line, just like in VS Code. CTRL + SHIFT + BACKSPACE by default. """
# this program is free to use
# feel free to change and redistribute anything from this program
# the code is not perfect, but short and simple using only the blender api

bl_info = {
    "name": "Text editor shortcut: Delete Line",
    "author": "Bambusak <bambusak85@gmail.com>",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "category": "shortcut",
    "location": "text editor",
    "description": "Adds the shortcut to the text editor to delete the current line, just like in VS Code. CTRL + SHIFT + BACKSPACE by default.",
}

if "bpy" in locals():
    import importlib
    importlib.reload(delete_line)
else:
    from . import delete_line

import bpy

def register():
    """ Registers the operator and adds the shortcut to the text editor. """
    bpy.utils.register_class(delete_line.TEXT_OT_DeleteLine)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Text", space_type='TEXT_EDITOR')
    # Set the shortcut to CTRL + SHIFT + BACKSPACE by default
    kmi = km.keymap_items.new(delete_line.TEXT_OT_DeleteLine.bl_idname, 'BACK_SPACE', 'PRESS', ctrl=True, shift=True)
    # asign the kmi
    kmi.active = True

def unregister():
    """ Unregisters the operator and removes the shortcut from the text editor. """
    bpy.utils.unregister_class(delete_line.TEXT_OT_DeleteLine)
