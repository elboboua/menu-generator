from typing import Union

from fastapi import FastAPI, staticfiles
from routes import auth_router, views_router



app = FastAPI()
app.mount("/static", staticfiles.StaticFiles(directory="static"), name="static")
app.include_router(views_router, tags=["views"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}