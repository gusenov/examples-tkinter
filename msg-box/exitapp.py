import tkinter as tk
from tkinter import messagebox


def exit_app():
    msg_box = tk.messagebox.askquestion('Exit App', 'Really Quit?', icon='error')
    if msg_box == 'yes':
        main_win.destroy()
    else:
        tk.messagebox.showinfo('Welcome Back', 'Welcome back to the App')


main_win = tk.Tk()
main_win.geometry('300x200')

btn = tk.Button(main_win, text='Exit App', command=exit_app)
btn.pack()

main_win.mainloop()
