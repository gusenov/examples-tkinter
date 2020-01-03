import tkinter as tk
from tkinter import ttk


def callback():
    # Получить текст можно с помощью вызова у StringVar метода get(),
    # а установить текст можно с помощью вызова метода set().
    # У объекта виджета Entry также есть метод get().
    result_str.set("{} - {}".format(land_str.get(),
                                    city_str.get()))


main_win = tk.Tk()
main_win.geometry('200x100')


lbl_land = tk.Label(main_win, text="Country")
lbl_land.grid(column=0, row=0, sticky=tk.W)

land_str = tk.StringVar()
land_str.set("KZ")  # установить значение по умолчанию.

entry_land = tk.Entry(main_win,
                      width=20,  # ширина: 20 символов.
                      textvariable=land_str)
entry_land.grid(column=1, row=0, padx=10)


lbl_city = tk.Label(main_win, text="City")
lbl_city.grid(column=0, row=1, sticky=tk.W)

city_str = tk.StringVar()
entry_city = tk.Entry(main_win, width=20, textvariable=city_str)
entry_city.insert(tk.END, "ALM")  # insert(index, string)
entry_city.grid(column=1, row=1, padx=10)


btn_result = tk.Button(main_win, text='Get Result', command=callback)
btn_result.grid(column=0, row=2, pady=10, sticky=tk.W)

result_str = tk.StringVar()
lbl_result = tk.Label(main_win, textvariable=result_str)
lbl_result.grid(column=1, row=2, padx=10, sticky=tk.W)


main_win.mainloop()
