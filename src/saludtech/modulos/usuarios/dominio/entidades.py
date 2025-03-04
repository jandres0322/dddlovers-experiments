import uuid
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Usuario(AgregacionRaiz):

    id: uuid.UUID = field(hash=True, default=None)
    nombre: str = field(default=None)
    correo: str = field(default=None)

    """ def change_password(self, new_password: str):
        self.password_hash = hash_function(new_password) """