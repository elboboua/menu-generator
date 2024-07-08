from .menu_generator import MenuGenerator
import marvin
from .types import BusinessInfo, MenuCategory, MenuItem


class MarvinMenuGenerator(MenuGenerator):

    def generate_categories(self, business_info: BusinessInfo) -> list[MenuCategory]:
        categories = marvin.generate(
            n=6,
            instructions=f"Generate menu categories base on the business info: {business_info}",
            target=MenuCategory,
        )
        return categories
    
    def generate_items(self, menu_category: MenuCategory, business_info: BusinessInfo) -> list[MenuItem]:
        items = marvin.generate(
            n=6,
            instructions=f"Generate menu items for the category {menu_category} for this restaurant: {business_info}",
            target=MenuItem,
        )
        return items


