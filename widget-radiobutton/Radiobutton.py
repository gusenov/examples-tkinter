import tkinter as tk

main_win = tk.Tk()
main_win.geometry('150x100')

# Также как и в случае с check button, radio-кнопкам нужно ассоциированное значение.
# Radio-кнопки в одной и той же группе используют общую переменную.
radio_val = tk.IntVar()

# Radio-кнопки в одной и той же группе должны иметь уникальные значения.
# Значение (value) выбранной radio-кнопки автоматически устанавливается в переменную radio_val.
radio1 = tk.Radiobutton(main_win,
                        text='January',
                        variable=radio_val,
                        value=1)

radio2 = tk.Radiobutton(main_win,
                        text='Febuary',
                        variable=radio_val,
                        value=2,
                        command=lambda: print(radio_val.get()))

radio3 = tk.Radiobutton(main_win,
                        text='March',
                        variable=radio_val,
                        value=3,
                        indicatoron=0)  # выключить круговой индикатор.
# По умолчанию индикатор radio-кнопки является кругом, но он может быть заменен прямоугольником содержащим текст
# или изображение.

radio1.grid(column=0, row=0)
radio2.grid(column=0, row=1)
radio3.grid(column=0, row=2)

# Текст метки автоматически отражает значение выбранной кнопки.
label_val = tk.Label(main_win,
                     textvariable=radio_val)  # такое же как и значение для опции variable у radio-кнопок.
label_val.grid(column=2, row=0, sticky="E", padx=40)

main_win.mainloop()
