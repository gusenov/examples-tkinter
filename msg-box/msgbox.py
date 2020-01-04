from tkinter import messagebox

messagebox.showinfo("Basic Example",  # заголовок.
                    "a Baisc Tk MessageBox")  # информация.

messagebox.showwarning("Warning Example", "Warning MessageBox")

messagebox.showerror("Error Example", "Error MessageBox")

messagebox.askquestion("Ask Question Example", "Quit?")

messagebox.askyesno("Ask Yes/No Example", "Quit?")

messagebox.askokcancel("Ask OK Cancel Example", "Quit?")

messagebox.askretrycancel("Ask Retry Cancel Example", "Quit?")
