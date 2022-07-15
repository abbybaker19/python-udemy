from tkinter import *
from tkinter import ttk


def set_entry(*args):
    entry_1_txt.set("hello")


def chk_but_changed(*args):
    entry_1_txt.set(chk_btn_1_txt.get())


def radio_changed(*args):
    entry_1_txt.set(radio_but_1_val.get())


def combo_changed(*args):
    entry_1_txt.set(combo_1_val.get())


root = Tk()
root.title("widget example")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_1_txt = StringVar()
label_1 = ttk.Label(frame, text='data: ')
label_1.grid(column=1, row=1, sticky=(W, E))

label_1['textvariable'] = label_1_txt
label_1_txt.set('data')

entry_1_txt = StringVar()
entry_1 = ttk.Entry(frame, width=7, textvariable=entry_1_txt)
entry_1.grid(column=2, row=1, sticky=(E, W))
entry_1_txt.set(label_1_txt.get())

button_1 = ttk.Button(frame, text='click', command=set_entry)
button_1.grid(column=3, row=1, sticky=(E, W))

# button_1['state'] = 'disabled'
button_1['state'] = 'enabled'

chk_btn_1_txt = StringVar()
chk_btn_1 = ttk.Checkbutton(frame, text='feeling', command=chk_but_changed, variable=chk_btn_1_txt, onvalue='happy',
                            offvalue='sad')
chk_btn_1.grid(column=4, row=1, sticky=(W, E))

# radio buttons
radio_but_1_val = StringVar()
red_r_but = ttk.Radiobutton(frame, text='red', variable=radio_but_1_val, value='red', command=radio_changed)
blue_r_but = ttk.Radiobutton(frame, text='blue', variable=radio_but_1_val, value='blue', command=radio_changed)
green_r_but = ttk.Radiobutton(frame, text='green', variable=radio_but_1_val, value='green', command=radio_changed)

red_r_but.grid(column=2, row=2, sticky=(E, W))
blue_r_but.grid(column=3, row=2, sticky=(E, W))
green_r_but.grid(column=4, row=2, sticky=(E, W))

label_2 = ttk.Label(frame, text='favorite color')
label_2.grid(column=1, row=2, sticky=(W, E))

# combo boxes
combo_1_val = StringVar()
combo_1 = ttk.Combobox(frame, textvariable=combo_1_val)
label_3 = ttk.Label(frame, text='size')
label_3.grid(column=1, row=3, sticky=(E, W))
combo_1['values'] = ('small', 'medium', 'large')
combo_1.grid(column=2, row=3, sticky=(W, E))
combo_1.bind('<<comboboxselected>>', combo_changed)

root.mainloop()
