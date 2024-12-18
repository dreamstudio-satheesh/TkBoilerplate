import importlib

class BaseController:
    def __init__(self, root):
        self.root = root

    def load_controller(self, controller_name, view_name):
        try:
            # Dynamically load the controller
            controller_module = importlib.import_module(f"controllers.{controller_name}")
            controller_class = getattr(controller_module, controller_name.capitalize())
            controller_instance = controller_class(self.root)

            # Convert the view name to snake_case for file import
            view_file_name = self._to_snake_case(view_name)

            # Dynamically load the view
            view_module = importlib.import_module(f"views.{view_file_name}")
            view_class = getattr(view_module, view_name)
            controller_instance.load_view(view_class)
        except Exception as e:
            print(f"Error loading {controller_name}: {e}")

    @staticmethod
    def _to_snake_case(name):
        # Convert PascalCase or CamelCase to snake_case
        import re
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
