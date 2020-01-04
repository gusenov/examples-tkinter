import tkinter as tk

main_win = tk.Tk()
main_win.geometry('300x200')
main_win.title("Basic Scale")

scale = tk.Scale(main_win,
                 orient='horizontal',  # по умолчанию ориентация = vertical.
                 resolution=0.1,  # по умолчанию = 1.
                 from_=0,  # минимальное значение.
                 to=10)  # максимальное значение.

scale.pack()

main_win.mainloop()
