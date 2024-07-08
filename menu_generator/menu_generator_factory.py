from .mock_menu_generator import MockMenuGenerator
from .marvin_menu_generator import MarvinMenuGenerator

class MenuGeneratorFactory:
    def create_menu_generator(self):
        # Generate the menu
        return MarvinMenuGenerator()