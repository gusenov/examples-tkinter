import tkinter as tk

main_win = tk.Tk()
main_win.geometry('300x300')

lbl_a = tk.Label(main_win, text ="Label (0, 0)", fg="blue", bg="#FF0")
lbl_b = tk.Label(main_win, text ="Label (20, 20)", fg="green", bg="#300")
lbl_c = tk.Label(main_win, text ="Label (40, 50)", fg="black", bg="#f03")
lbl_d = tk.Label(main_win, text ="Label (0.5, 0.5)", fg="orange", bg="#0ff")

lbl_a.place(x=0, y=0)  # абсолютная позиция виджета в px.
lbl_b.place(x=20, y=20)
lbl_c.place(x=40, y=50)

# Относительная позиция:
lbl_d.place(relx=0.5,  # значения в диапазоне [0.0; 1.0]
            rely=0.5)
# relx=0.5, rely=0.5 означает, что виджет разместится в 50% ширины/высоты окна.
# relx=1.0 - правая граница окна.
# rely=1.0 - нижняя граница окна.

main_win.mainloop()
