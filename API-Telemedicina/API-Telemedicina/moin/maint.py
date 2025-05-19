from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_secreta_segura_123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )

import logging
logging.basicConfig(level=logging.INFO)












from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


fake_items_db = [
    {"id": 1, "name": "Item Uno", "description": "Descripción del ítem uno", "price": 10.5, "tax": 1.5},
    {"id": 2, "name": "Item Dos", "description": "Descripción del ítem dos", "price": 20.0, "tax": 2.0},
]

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}

@app.get("/items/")
async def read_items():
    return fake_items_db

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in fake_items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.post("/items/", response_model=Item)




@app.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item.dict())
    return item
@app.post("/login")
def login(user: UsuarioLogin):
    if user.email == "" or user.password == "":
        raise HTTPException(status_code=400, detail="Campos vacíos no permitidos")
    # Aquí agregas tu lógica real
    return {"msg": "Login exitoso"}

@app.get("/usuarios", tags=["Usuarios"], summary="Listar todos los usuarios")


