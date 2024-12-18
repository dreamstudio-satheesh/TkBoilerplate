import tkinter as tk

class DashboardView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Welcome to the Dashboard", font=("Arial", 24)).pack(pady=20)

        # Example: Add some buttons or widgets
        tk.Button(self, text="Logout", command=self.logout).pack(pady=10)

    def logout(self):
        # Redirect to LoginView on logout
        from views.login_view import LoginView
        self.controller.load_view(LoginView)
