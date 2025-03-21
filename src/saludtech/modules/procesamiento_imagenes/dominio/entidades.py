from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.entidades import AgregacionRaiz, Entidad
import uuid

@dataclass
class ImagenProcesada(Entidad):
    ruta_storage: str = field(default_factory=str)
    ruta_thumbanil: str = field(default_factory=str)
    ruta_metadatos: str = field(default_factory=str)


@dataclass
class PaqueteDescarga(AgregacionRaiz):
    id_solicitud: str = field(hash=True, default_factory=str)
    ruta_comprimido: str = field(default_factory=str)
    
    def generar_comprimido(self, imagenes: list[ImagenProcesada]):
        self.ruta_comprimido = f"{self.id_solicitud}.zip"
        pass