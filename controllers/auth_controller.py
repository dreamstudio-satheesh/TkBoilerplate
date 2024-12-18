from models.user import User

class Auth_controller:
    def __init__(self, root):
        self.root = root
        self.user_model = User()

    def load_view(self, view_class):
        # Clear existing frames
        for widget in self.root.winfo_children():
            widget.destroy()

        # Load the provided view
        view = view_class(self.root, self)
        view.pack(fill="both", expand=True)

    def login(self, username, password):
        if self.user_model.authenticate(username, password):
            # Load DashboardView upon successful login
            from views.dashboard_view import DashboardView
            self.load_view(DashboardView)
            return True
        return False
