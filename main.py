from typing import List
from uuid import uuid4, UUID
from models import Genero, Role, User
from fastapi import FastAPI, HTTPException

# Crear la aplicación de FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"Saludo": "Hola amigos del yutu"}

# Base de datos simulada
db: List[User] = [
    User(
        id=uuid4(),
        nombre="Marco",
        apellidos="Reyes",
        genero=Genero.masculino,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        nombre="Carolina",
        apellidos="Arias",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        nombre="Luis",
        apellidos="Fernández",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        nombre="Ana",
        apellidos="López",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
]

@app.get("/api/users")
async def get_users():
    return db

@app.post("/api/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    """
    Elimina un usuario de la base de datos.
    Args:
        user_id (UUID): ID del usuario a eliminar.
    Returns:
        dict: Confirmación de eliminación.
    """
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"Usuario con ID {user_id} eliminado correctamente."}
    
    # Si no se encuentra el usuario, lanzar una excepción
    raise HTTPException(status_code=404, detail=f"Usuario con ID {user_id} no encontrado.")
