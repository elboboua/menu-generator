from typing import Union

from fastapi import FastAPI
from routes import auth_router
from menu_generator import MenuGeneratorFactory, BusinessInfo

mg = MenuGeneratorFactory().create_menu_generator()

# business_info = BusinessInfo(name="Dave's Gourmet Burgers", description="The highest quality burgers this side of the smoky mountains!", city="San Francisco", cost_level=5)
# categories = mg.generate_categories(business_info)
# for category in categories:
#     print(category)
#     items = mg.generate_items(category, business_info)
#     for item in items:
#         print("\t",item)


app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}