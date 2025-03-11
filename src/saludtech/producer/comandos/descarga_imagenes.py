
from dataclasses import dataclass
from saludtech.seedwork.aplicacion.comandos import Comando


@dataclass
class DescargarImagen(Comando):
    path: str
    imagenes: list[]