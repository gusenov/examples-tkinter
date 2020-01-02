from sys import version_info

if version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

app_window = tk.Tk()  # главное родительское окно.
app_window.title("Hello World")
app_window.mainloop()  # позволить окну войти в бесконечный цикл.
