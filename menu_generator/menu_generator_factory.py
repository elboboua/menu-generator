from .mock_menu_generator import MockMenuGenerator

class MenuGeneratorFactory:
    def create_menu_generator(self):
        # Generate the menu
        return MockMenuGenerator()