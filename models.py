from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Genero(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    otro = "otro"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre: str  # Anotación de tipo corregida
    apellidos: str  # Anotación de tipo corregida
    genero: Genero  # Anotación de tipo corregida
    roles: List[Role]  # Anotación de tipo corregida
