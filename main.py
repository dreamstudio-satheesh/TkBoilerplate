import tkinter as tk
from utils.menu_manager import MenuManager
from controllers.base_controller import BaseController

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Boilerplate App")
        self.geometry("800x600")

        # Initialize Menu Manager
        self.menu_manager = MenuManager(self)
        self.menu_manager.setup_menu()

        # Initialize Router
        self.router = BaseController(self)

        # Load Default View (Login)
        self.router.load_controller("auth_controller", "LoginView")

if __name__ == "__main__":
    app = App()
    app.mainloop()
