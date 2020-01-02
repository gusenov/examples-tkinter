from sys import version_info
from functools import partial

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

main_window = tk.Tk()

label = tk.Label(main_window, text="0")


def change_label_number(num=1):
    counter = int(str(label['text']))
    counter += num
    label.config(text=str(counter))


button_inc = tk.Button(main_window,
                       text="Increase",
                       width=30,
                       command=change_label_number)  # binding между кнопкой и callback-функцией.

button_dec = tk.Button(main_window,
                       text="Decrease",
                       width=30,
                       default="active",
                       command=partial(change_label_number, -1))
# Чтобы передать аргументы в callback-функцию нужен объект partial из functools.
# partial-объекты являются callable-объектами с позиционными аргументами args и keyword-аргументами keywords.

button_inc.pack(side=tk.LEFT)
button_dec.pack(side=tk.LEFT)

label.pack()

main_window.mainloop()
