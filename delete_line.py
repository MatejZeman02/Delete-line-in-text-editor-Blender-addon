""" class TEXT_OT_DeleteLine(bpy.types.Operator) """
import bpy

class TEXT_OT_DeleteLine(bpy.types.Operator):
    """ Operator which deletes the current line in the text editor. """
    bl_idname = "text.delete_line"
    bl_label = "Delete line"
    bl_context = "text" # Restrict the operator to the Text Editor context

    @classmethod
    def add_newline(cls, context):
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
        bpy.ops.text.cut() # cut the line
        # delete left newline character
        bpy.ops.text.delete(type='NEXT_CHARACTER')

    def execute(self, context):
        """ Executes the operator. """
        self.delete_line(context)

        return {'FINISHED'}
