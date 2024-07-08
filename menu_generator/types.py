from pydantic import BaseModel, Field

class BusinessInfo(BaseModel):
    name: str
    description: str
    city: str
    cost_level: int = Field(description="A number from 1 to 5 indicating the cost level of the restaurant. 1 is the least expensive, 5 is the most expensive.")

    def __repr__(self) -> str:
        return f"{self.name} - {self.description} - {self.city} - {self.cost_level}/5"

class MenuCategory(BaseModel):
    name: str = Field(description="The name of a category of a menu. For example, 'Appetizers', 'Entrees', or 'Desserts'.")
    description: str = Field(description="A short menu-friendly description of the category.")

    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"

class MenuItem(BaseModel):
    name: str = Field(description="The name of a menu item. For example, 'Spring Rolls', 'Pad Thai', or 'Cheesecake'.")
    description: str = Field(description="A description of the menu item.")
    price: float = Field(description="The price of the menu item.")

class Menu(BaseModel):
    business_info: BusinessInfo
    categories: list[MenuCategory]
    items: list[MenuItem]