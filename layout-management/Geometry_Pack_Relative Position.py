import tkinter as tk

main_win = tk.Tk()
main_win.geometry('1000x200')


btn_west = tk.Button(main_win, text="West", width=15)
# Привязка в левой стороне окна:
btn_west.pack(side='left',
              ipadx=20,  # внутренний отступ (inner padding) в px.
              padx=30)  # внешний отступ (outer padding) в px.


btn_east_1 = tk.Button(main_win, text="East 1", width=15)
# Привязка к правой стороне окна:
btn_east_1.pack(side='right', ipadx=20, padx=30)


btn_east_2 = tk.Button(main_win, text="East 2", width=15)
btn_east_2.pack(side='right', ipadx=20, padx=30)


main_win.mainloop()
