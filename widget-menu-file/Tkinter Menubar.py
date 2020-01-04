import tkinter as tk
from tkinter import filedialog


def on_open():
    print(filedialog.askopenfilename(initialdir="/",
                                     title="Open file",
                                     filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def on_save():
    print(filedialog.asksaveasfilename(initialdir="/",
                                       title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


main_win = tk.Tk()
main_win.geometry('300x200')
main_win.title("Basic Menu Bar")

# Нужно передать в конструктор меню родительский виджет.
menu_bar = tk.Menu(main_win)

file_menu = tk.Menu(menu_bar,
                    tearoff=0)
# Когда tearoff=1, то меню можно открепить от главного окна, чтобы оно стало плавающим.

file_menu.add_command(label="Open", command=on_open)
file_menu.add_command(label="Save", command=on_save)
file_menu.add_command(label="Exit", command=main_win.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Несмотря на то, что menu_bar был создан как дочерний виджет main_win,
# всё равно нужно его сконфигурировать как меню.
main_win.config(menu=menu_bar)

main_win.mainloop()
