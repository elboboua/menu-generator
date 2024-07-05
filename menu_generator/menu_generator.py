from abc import ABC, abstractmethod
from .types import BusinessInfo, MenuCategory, MenuItem


class MenuGenerator(ABC):
    @abstractmethod
    def generate_categories(self, business_info: BusinessInfo) -> list[MenuCategory]:
        pass
    
    @abstractmethod
    def generate_items(self, menu_category: MenuCategory) -> list[MenuItem]:
        pass


