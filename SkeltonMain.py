# coding=utf-8
import tkinter
from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Esc button to quit
        self.master.bind("<Escape>", lambda x: self.master.destroy())

        # title
        version = Tcl().eval('info patchlevel')
        self.master.title(f"Python GUI: {version}")

        # form size and position
        self.master.geometry("320x240+50+50")
        self.grid(sticky=N+S+E+W)

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        quit_button = Button(self, text="Submit", command=self._submit)
        quit_button.grid(column=2, row=0)

        ttk.Label(self, text="Keyword: ").grid(column=0, row=0)
        name = tkinter.StringVar
        entered = ttk.Entry(self, textvariable=name)
        entered.grid(column=1, row=0)

        entered.focus()

    def create_menu(self):
        top = self.winfo_toplevel()
        menu_bar = Menu(top)
        top['menu'] = menu_bar
        sub_menu = Menu(menu_bar)
        menu_bar.add_cascade(label='File', menu=sub_menu)
        sub_menu.add_command(label='Quit', command=self._quit)

    def _quit(self):
        self.master.quit()
        self.master.destroy()
        exit()

    @staticmethod
    def _submit():
        print("Submit")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
