from tkinter import Tk
import asyncio
from controller import Controller
from gui_login import LoginGUI
from gui_loading import LoadingGUI
from gui_main import MainGUI

# user: 6e749bf8f1de42e8a3ce17507f40ca7c
# pword: 67c5ec0b43724a4cba0f4e34e458bd38


class View:
    def __init__(self):
        self._controller = Controller()
        self.root = Tk()
        self.set_root()

    def login_GUI(self):
        self.login_window = LoginGUI(self.root)
        self.login_window.button_auth.bind("<ButtonPress-1>", self.get_entries, True)
        self.login_window.button_auth.bind("<ButtonPress-1>", self.loading_GUI, True)
        # self.login_window.button_auth.bind("<Destroy>", self._controller.data_collect)

    # aparece nova tela de loading
    def loading_GUI(self, event):
        self.window_cleaner(self.login_window)
        self.load_window = LoadingGUI(self.root)

        self.load_window.progress_bar.start(1000)
        if self.load_window.progress_bar.instate():
            async_task = asyncio.create_task(self._controller.data_collect())
            asyncio.run(async_task())
            print("rodou")
        # self.load_window.progress_bar.bind("<Activate>", self._controller.data_collect)
        self.load_window.progress_bar.stop()
        # self.load_window.progress_bar.state()
        self.load_window.progress_bar.after(5000, self.main_GUI)

    # aparece nova tela com conteudo
    def main_GUI(self):
        self.window_cleaner(self.load_window)
        self.load_window = MainGUI(self.root)

    def get_entries(self, event):
        name = self.login_window.entry_name.get()
        password = self.login_window.entry_password.get()
        return self._controller.verify_entries(name, password)

    def window_cleaner(self, window):
        for widget in window.content_box.winfo_children():
            widget.destroy()
        window.content_box.destroy()

    def set_root(self):
        self.root.title("Spotify Project")
        # self.root.iconbitmap('./icon.ico')
        self.root.geometry("1200x768")
        # root.attributes("-alpha", 0.97)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.configure(background="grey10")


# root = Tk()
# l = ttk.Label(root, text="Starting...")
# l.grid()
# l.bind("<Enter>", lambda e: l.configure(text="Moved mouse inside"))
# l.bind("<Leave>", lambda e: l.configure(text="Moved mouse outside"))
# l.bind("<ButtonPress-1>", lambda e: l.configure(text="Clicked left mouse button"))
# l.bind("<3>", lambda e: l.configure(text="Clicked right mouse button"))
# l.bind("<Double-1>", lambda e: l.configure(text="Double clicked"))
# l.bind(
#     "<B3-Motion>", lambda e: l.configure(text="right button drag to %d,%d" % (e.x, e.y))
# )
# root.mainloop()
