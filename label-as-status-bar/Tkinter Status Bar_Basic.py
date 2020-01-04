import tkinter as tk

app_win = tk.Tk()
app_win.geometry('300x200')
app_win.title("Basic Status Bar")

status_bar = tk.Label(app_win,
                      text="on the way…",
                      bd=1,  # размер рамки.
                      relief=tk.SUNKEN,  # при "впалом" виде выглядит как часть окна.
                      anchor=tk.W)  # выравнивание текста внутри метки.

status_bar.pack(side=tk.BOTTOM,  # спозиционировать внизу GUI.
                fill=tk.X)  # покрыть всю ширину окна.

app_win.mainloop()
