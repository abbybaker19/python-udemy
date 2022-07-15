from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def quit_app():
    root.quit()


def show_about(event=None):
    messagebox.showwarning("about", "isn't this a fun program?")


def change_font(event=None):
    print("font changed to", text_font.get())


root = Tk()
root.title("menu bar example")
the_menu = Menu(root)

# ---- file ----
file_menu = Menu(the_menu, tearoff=0)
file_menu.add_command(label="open")
file_menu.add_command(label="save")
file_menu.add_separator()
the_menu.add_cascade(label="file", menu=file_menu)

# ---- view ----
view_menu = Menu(the_menu, tearoff=0)
line_numbers = IntVar()
line_numbers.set(1)
view_menu.add_checkbutton(label="line numbers", variable=line_numbers)
the_menu.add_cascade(label="view", menu=view_menu)

# ---- font ----
text_font = StringVar()
text_font.set("times")
font_menu = Menu(the_menu, tearoff=0)
font_menu.add_radiobutton(label="times", variable=text_font, command=change_font)
font_menu.add_radiobutton(label="courier", variable=text_font, command=change_font)
font_menu.add_radiobutton(label="arial", variable=text_font, command=change_font)
the_menu.add_cascade(label="font", menu=font_menu)

# ---- help ----
help_menu = Menu(the_menu, tearoff=0)
help_menu.add_command(label="about", accelerator="control-A", command=show_about)
the_menu.add_cascade(label="help", menu=help_menu)
root.bind('<Control-A>', show_about)
root.bind('<Control-a>', show_about)

root.config(menu=the_menu)

root.mainloop()
