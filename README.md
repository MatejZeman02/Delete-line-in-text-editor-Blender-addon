# Delete line in text editor - Blender addon
Adds missing shortcut for deleting the line which behaves just like in the VS Code. So you can paste it afterwards.


![showcase img](showcase.jpg)

***

## Install
  
  1. **Download**
    - Go to releases and download `zip` folder of the newest version.
    - Or download git repo as `zip`.
  
  2. **Open the Blender**
  
  3. **Open:** Preferences > Addons/Extensions
  
  4. **Install** an addon via button (top right corner).
  
  5. **Select** the downloaded `.zip` file.
  
  6. **Check** the box next to the extension's name.

## Addon description
A small addon that adds the funcionality of deleting the current line in the text editor.  And it is also cuting the content into the clipboard. This means you can then paste the deleted line wherever you want.

You do not need to select anything. Just press `CTRL + SHIFT + BACKSPACE` while in the text editor on some line. The shortcut can be changed in the preferences.

### How it works?

The shortcut is then editable in the Blenders settings: "Edit > Preferences > Keymap > Text > Text global > Delete line". The way it works is mostly using Blenders built in functions:

1. Adding newline character to the current line.

2. Selecting the whole line.

3.  Cutting the selected content.

4. Deleting the remaining newline character.

***

**Video:**
Video showcase on [youtube](https://www.youtube.com/watch?v=-JpoWFsWgH4).
