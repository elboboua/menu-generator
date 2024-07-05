from pydantic import BaseModel

class BusinessInfo(BaseModel):
    name: str
    description: str
    city: str

class MenuCategory(BaseModel):
    name: str
    description: str

class MenuItem(BaseModel):
    name: str
    description: str
    price: float

class Menu(BaseModel):
    business_info: BusinessInfo
    categories: list[MenuCategory]
    items: list[MenuItem]