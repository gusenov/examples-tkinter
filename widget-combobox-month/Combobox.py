import tkinter as tk
from tkinter import ttk  # combobox widget находится в модуле ttk.
from pprint import pprint


def callback(event):  # аргумент event передается из combobox virtual event.
    print("New Element Selected")


# Выполняется перед отображением pop-down списка пунктов выбора:
def change():
    combo["values"] = ["July", "August", "September", "October"]


main_win = tk.Tk()
main_win.geometry('200x100')

lbl = tk.Label(main_win,
               text="Choose your favourite month")
lbl.grid(column=0, row=0)

combo = ttk.Combobox(main_win,
                     values=["January", "February", "March", "April"],
                     postcommand=change)  # динамическое обновление пунктов выбора.
pprint(dict(combo))
'''
{'background': '',
 'class': '',
 'cursor': '',
 'exportselection': 1,
 'font': <font object: 'TkTextFont'>,
 'foreground': '',
 'height': '10',
 'invalidcommand': '',
 'justify': 'left',
 'postcommand': '139782274296648change',
 'show': '',
 'state': <index object: 'normal'>,
 'style': '',
 'takefocus': 'ttk::takefocus',
 'textvariable': '',
 'validate': 'none',
 'validatecommand': '',
 'values': ('January', 'February', 'March', 'April'),
 'width': 20,
 'xscrollcommand': ''}
'''

combo.grid(column=0, row=1)
combo.current(1)  # выбрать элемент по умолчанию.

print(combo.current(),  # получить индекс текущего выбранного элемента.
      combo.get())  # получить сам элемент.

# Связать callback-функцию и combobox virtual event:
combo.bind("<<ComboboxSelected>>", callback)

main_win.mainloop()
