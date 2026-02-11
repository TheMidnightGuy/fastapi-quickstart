#Obtenemos resultados en http://127.0.0.1:8000/users/me

from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}