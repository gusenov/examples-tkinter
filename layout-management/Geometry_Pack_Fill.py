import tkinter as tk

main_win = tk.Tk()
main_win.geometry('300x200')

btn_x = tk.Button(main_win,
                  text="Fill X",
                  bg="red",
                  height=5)
btn_x.pack(fill='x')  # заполнить по ширине всего окна.

btn_y = tk.Button(main_win,
                  text="Fill Y",
                  bg="green",
                  width=10)
btn_y.pack(side='left',
           fill='y')  # заполнить по высоте всего окна.

# fill='both' для того чтобы заполнить и по ширине и по высоте.

main_win.mainloop()
