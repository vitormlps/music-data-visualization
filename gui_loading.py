from tkinter import *
from tkinter import ttk


class LoadingGUI:
    def __init__(self, master: Tk) -> None:
        self.content_box = ttk.Frame(master, padding=(12, 8))
        self.set_content_box()

        self.set_title()
        self.set_progress_bar()

    def set_content_box(self):
        self.content_box.grid(column=0, row=0)
        # self.content_box.columnconfigure(0, weight=1)
        # self.content_box.columnconfigure(1, weight=1)
        # self.content_box.rowconfigure(0, weight=2)
        # self.content_box.rowconfigure(1, weight=2)
        # self.content_box.configure(height=768, width=1200)

    def set_title(self):
        self.title = ttk.Label(self.content_box)
        self.title["text"] = "Loading..."
        self.title.grid(column=0, row=0, sticky=(S))

    def set_progress_bar(self):
        self.progress_bar = ttk.Progressbar(self.content_box)
        self.progress_bar["orient"] = HORIZONTAL
        self.progress_bar["mode"] = "determinate"
        self.progress_bar["length"] = 100
        self.progress_bar.grid(column=0, row=1, sticky=(N))
