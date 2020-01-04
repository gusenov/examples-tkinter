import tkinter as tk


class ScrollbarWithListbox:
    def __init__(self):
        self.window = tk.Tk()

        # Инстанцировать экземпляр Scrollbar:
        self.scrollbar = tk.Scrollbar(self.window)

        self.scrollbar.pack(side="right",
                            fill="y")

        self.listbox = tk.Listbox(self.window,
                                  yscrollcommand=self.scrollbar.set)
        # yscrollcommand это опция прокручиваемых виджетов, которая управляется
        # scrollbar-ом и используется для коммуникации с вертикальной полосой прокрутки.

        for i in range(100):
            self.listbox.insert("end", str(i))

        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)
        # Когда пользователь двигает slider у Scrollbar,
        # то вызывается метод yview с соответствующим аргументом.

        self.window.mainloop()


if __name__ == '__main__':
    app = ScrollbarWithListbox()
