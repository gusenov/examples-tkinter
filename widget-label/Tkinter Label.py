from sys import version_info
from pprint import pprint

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
    from tkinter import font as tkFont

main_window = tk.Tk()

label_widget_1 = tk.Label(main_window,
                          text="This is a Label",
                          height=15,
                          width=100,
                          font=("Times", 20, "italic"),
                          bg="black",
                          fg="gold")
label_widget_1.pack()  # pack() управляет layout-ом виджета в родительском виджете.


pprint(dict(label_widget_1))  # получить и вывести свойства label.
'''
{'activebackground': '#ececec',
 'activeforeground': '#000000',
 'anchor': 'center',
 'background': 'black',
 'bd': <pixel object: '1'>,
 'bg': 'black',
 'bitmap': '',
 'borderwidth': <pixel object: '1'>,
 'compound': 'none',
 'cursor': '',
 'disabledforeground': '#a3a3a3',
 'fg': 'gold',
 'font': 'Times 20 italic',
 'foreground': 'gold',
 'height': 15,
 'highlightbackground': '#d9d9d9',
 'highlightcolor': '#000000',
 'highlightthickness': <pixel object: '0'>,
 'image': '',
 'justify': 'center',
 'padx': <pixel object: '1'>,
 'pady': <pixel object: '1'>,
 'relief': 'flat',
 'state': 'normal',
 'takefocus': '0',
 'text': 'This is a Label',
 'textvariable': '',
 'underline': -1,
 'width': 100,
 'wraplength': <pixel object: '0'>}
'''


labelFont2 = tkFont.Font(family="Helvetica",
                         size=20,
                         weight=tkFont.BOLD,
                         underline=1,
                         overstrike=1)
label_widget_2 = tk.Label(main_window,
                          text="Customized Label",
                          font=labelFont2)
label_widget_2.pack()


pprint(tkFont.families())  # вывести доступные семейства шрифтов.


image = tk.PhotoImage(file='calendar-icon.png')
# tk.PhotoImage генерирует
# _tkinter.TclError: couldn't recognize data in image file
# если не может распознать формат изображения.

label_image = tk.Label(main_window,
                       image=image)  # свойство image используется для отображения изображений.
label_image.pack()


main_window.mainloop()
