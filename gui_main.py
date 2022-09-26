from tkinter import *
from tkinter import ttk


class MainGUI:
    def __init__(self, master: Tk) -> None:
        self.content_box = ttk.Frame(master, padding=(12, 8))
        self.set_content_box()

        self.set_title()

        self.set_quit_button()

    def set_content_box(self):
        self.content_box.grid(column=0, row=0)
        # Usar column e row configure para modificar o resizing behavior.
        # self.content_box.columnconfigure(0, weight=1)
        # self.content_box.rowconfigure(0, weight=2)

    def set_title(self):
        self.title = ttk.Label(self.content_box)
        self.title["text"] = "Main GUI"
        self.title.grid(column=0, row=0, sticky=(W))

    def set_quit_button(self):
        self.quit_button = ttk.Button(self.content_box)
        self.quit_button["text"] = "Quit"
        self.quit_button["width"] = 20
        self.quit_button["command"] = self.content_box.quit
        self.quit_button.grid(column=0, row=4, sticky=W)
