import tkinter as tk


def callback():
    print("Clicked!")


app_win = tk.Tk()
app_win.geometry('150x100')


# Каждый checkbutton должен быть ассоциирован с переменной.
chk_val_1 = tk.BooleanVar()
chk_val_1.set(True)

chk_btn_1 = tk.Checkbutton(app_win,
                           text='Check Box',
                           var=chk_val_1,
                           command=callback)  # при переключении состояния вызывается callback.

# grid это другой тип layout manager-а помимо pack.
# В Tkinter есть 3 layout/geometry manager-a: pack, grid и place.
chk_btn_1.grid(column=0, row=0)

# Выбрать и убрать выделение можно с помощью методов select() и deselect().
# Получить значение checkbutton можно с помощью вызова метода get().

chk_btn_1.deselect()
print("The checkbutton value when deselected is {}".format(chk_val_1.get()))
# The checkbutton value when deselected is False

chk_btn_1.select()
print("The checkbutton value when selected is {}".format(chk_val_1.get()))
# The checkbutton value when selected is True

# Состояние check button также может быть переключено с помощью метода toggle().

chk_btn_1.toggle()
print("The checkbutton value after toggled is {}".format(chk_val_1.get()))
# The checkbutton value after toggled is False


chk_val_2 = tk.StringVar()
chk_btn_2 = tk.Checkbutton(app_win,
                           text='Check Box',
                           var=chk_val_2,
                           onvalue="RGB",  # значение для состояния selected.
                           offvalue="YCbCr")  # значение для состояния non-selected.
# Тип данных ассоциированный с check button должен быть тем же самым, что и у значений в onvalue и offvalue.
# Иначе будет ошибка: _tkinter.TclError

chk_btn_2.grid(column=0, row=1)

chk_btn_2.select()
print("The checkbutton value when selected is {}".format(chk_val_2.get()))
# The checkbutton value when selected is RGB

chk_btn_2.deselect()
print("The checkbutton value when deselected is {}".format(chk_val_2.get()))
# The checkbutton value when deselected is YCbCr


app_win.mainloop()
