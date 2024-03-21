""" class TEXT_OT_DeleteLine(bpy.types.Operator) """
import bpy

class TEXT_OT_DeleteLine(bpy.types.Operator):
    """ Operator which deletes the current line in the text editor. """
    bl_idname = "text.delete_line"
    bl_label = "Delete line"
    bl_context = "text"

    @staticmethod
    def add_newline(context):
        """ Adds a newline character to the end of the selected line. """
        text = context.space_data.text
        current_line_index = context.space_data.text.current_line_index

        # Check if the current line index is valid
        if 0 <= current_line_index < len(text.lines):
            current_line = text.lines[current_line_index]

            # Add a newline character to the end of the selected line
            current_line.body += "\n"

    @classmethod
    def delete_line(cls, context):
        """ Deletes the current line in the text editor. """
        cls.add_newline(context) # add newline to the end of the line

        bpy.ops.text.select_line() # select the line
        bpy.ops.text.cut() # cut the line, just like CTRL+X
        # Delete left newline character
        bpy.ops.text.delete(type='NEXT_CHARACTER')

    @staticmethod
    def create_shortcut():
        """ adds the shortcut to the text editor. """
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name="Text", space_type='TEXT_EDITOR')
        # Set the shortcut to CTRL + SHIFT + BACKSPACE by default
        kmi = km.keymap_items.new(TEXT_OT_DeleteLine.bl_idname, 'BACK_SPACE', 'PRESS', ctrl=True, shift=True)
        # Asign the kmi
        kmi.active = True

    @staticmethod
    def remove_shortcut():
        """ Removes the shortcut from the text editor. """
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps['Text']
        for kmi in km.keymap_items:
            if kmi.idname == TEXT_OT_DeleteLine.bl_idname:
                km.keymap_items.remove(kmi)
                break

    def execute(self, context):
        """ Executes the operator. """
        self.delete_line(context)

        return {'FINISHED'}
