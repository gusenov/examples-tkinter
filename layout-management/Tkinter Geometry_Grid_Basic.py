import tkinter as tk

main_win = tk.Tk()


lbl_width = tk.Label(main_win, text ="Width Ratio")

# Каждый виджет должен быть помещен в ячейку.
# Координаты начинаются в левом верхнем углу окна.

lbl_width.grid(column=0, row=0,  # координаты ячейки.
               ipadx=5, pady=5,
               sticky=tk.W + tk.N)

entry_width = tk.Entry(main_win, width=20)
entry_height = tk.Entry(main_win, width=20)


lbl_height = tk.Label(main_win, text ="Height Ratio")
lbl_height.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W + tk.S)

entry_width.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
entry_height.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)


btn_res = tk.Button(main_win, text ='Get Result')
btn_res.grid(column=0, row=2, pady=10, sticky=tk.W)


img_logo = tk.PhotoImage(file='Letter-A-grey-icon.gif')
lbl_logo = tk.Label(main_win, image=img_logo)

lbl_logo.grid(row=0, column=2,
              columnspan=2, rowspan=2,  # объединение ячеек.
              sticky=tk.W+tk.E+tk.N+tk.S,
              padx=5, pady=5)


main_win.mainloop()
