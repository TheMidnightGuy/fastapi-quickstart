#Obtenemos resultados en http://127.0.0.1:8000/

from fastapi import FastAPI # pyright: ignore
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}