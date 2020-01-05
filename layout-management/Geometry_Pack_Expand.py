import tkinter as tk
import calendar

main_win = tk.Tk()

btn = tk.Button(main_win, text="Label ", bg="blue", height=5)
btn.pack(fill='x')

list_box = tk.Listbox(main_win, width=10)
list_box.pack(fill='both',
              expand=1)  # автоматическое расширение.
# Если expand=True или 1, то list box будет отображать все элементы от January до December.
# Иначе list box покажет только первые 10 элементов по умолчанию.

for i in range(1, 13):
    list_box.insert(tk.END, calendar.month_name[i])

main_win.mainloop()
