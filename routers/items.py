#Obtenemos resultados en http://127.0.0.1:8000/items/3

from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}