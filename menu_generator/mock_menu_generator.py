from .menu_generator import MenuGenerator

class MockMenuGenerator(MenuGenerator):
    def generate_categories(self, _):
        return [
            {"name": "Appetizers"},
            {"name": "Entrees"},
            {"name": "Desserts"},
        ]
    
    def generate_items(self, _):
        return [
            {"name": "Spring Rolls", "price": 5.99},
            {"name": "Pad Thai", "price": 12.99},
            {"name": "Cheesecake", "price": 4.99},
        ]