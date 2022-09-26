from view import View

# design pattern Model-View-Controller
def main():
    view = View()
    view.login_GUI()
    view.root.mainloop()


if __name__ == "__main__":
    main()
