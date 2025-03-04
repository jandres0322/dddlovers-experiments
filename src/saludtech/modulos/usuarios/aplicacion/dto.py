from dataclasses import dataclass
import uuid
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class UsuarioDTO(DTO):
    id: uuid.UUID
    nombre: str
    correo: str