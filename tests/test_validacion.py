##Se validan las funciones de FastAPI con PyTest
#Funciones validadas 
# endpoints basicos (GET)
# endpoints con query params
# endpoints con response model
# status codes

from fastapi.testclient import TestClient #type: ignore
from app.main import app

client = TestClient(app)

fake_token = "/?token=token-query"

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello Bigger Applications!"}

def test_read_users():
    response = client.get(f"/users", {fake_token})
    assert response.status_code == 200
    assert response.json() == [{"username":"Rick"},{"username":"Morty"}]

def test_read_items():
    response = client.get(f"/items", {fake_token})
    assert response.status_code == 200
    assert response.json() == {"Agua": {"name": "Agua Mineral"},"Cereal": {"name": "Cereal"}}
