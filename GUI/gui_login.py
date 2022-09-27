from tkinter import *
from tkinter import ttk


class LoginGUI:
    def __init__(self, master: Tk) -> None:
        self.content_box = ttk.Frame(master, padding=(12, 8))
        self.set_content_box()

        self.set_title()

        self.set_name_label()
        self.set_name_entry()

        self.set_password_label()
        self.set_password_entry()

        self.set_authentication_button()
        self.set_authentication_msg()

        self.set_quit_button()

    def set_content_box(self):
        self.content_box.grid(column=0, row=0)
        # Usar column e row configure para modificar o resizing behavior.
        # self.content_box.columnconfigure(0, weight=1)
        # self.content_box.rowconfigure(0, weight=2)

    def set_title(self):
        self.title = ttk.Label(self.content_box)
        self.title["text"] = "User log-in"
        self.title.grid(column=0, row=0, sticky=(W))

    def set_name_label(self):
        self.label_name = ttk.Label(self.content_box)
        self.label_name["text"] = "Name"
        # self.label_name["font"] = "TkDefaultFont"
        # self.label_name["borderwidth"] = 2
        # self.label_name["relief"] = "raised"
        self.label_name.grid(column=0, row=1, sticky=(E))

    def set_name_entry(self):
        self.entry_name = ttk.Entry(self.content_box)
        self.entry_name["width"] = 30
        self.entry_name.grid(column=1, row=1, sticky=(W))

    def set_password_label(self):
        self.label_password = ttk.Label(self.content_box)
        self.label_password["text"] = "Password"
        self.label_password.grid(column=0, row=2, sticky=(E))

    def set_password_entry(self):
        self.entry_password = ttk.Entry(self.content_box)
        self.entry_password["width"] = 30
        self.entry_password["show"] = "*"
        self.entry_password.grid(column=1, row=2, sticky=(W))

    def set_authentication_button(self):
        self.button_auth = ttk.Button(self.content_box)
        self.button_auth["text"] = "Login"
        self.button_auth["width"] = 20
        self.button_auth.grid(column=0, row=3, sticky=W)

    def set_authentication_msg(self):
        self.msg_auth_ok = Label(self.content_box, text="")
        self.msg_auth_ok.grid(column=1, row=3, sticky=(W))

    def set_quit_button(self):
        self.quit_button = ttk.Button(self.content_box)
        self.quit_button["text"] = "Quit"
        self.quit_button["width"] = 20
        self.quit_button["command"] = self.content_box.quit
        self.quit_button.grid(column=0, row=4, sticky=W)
