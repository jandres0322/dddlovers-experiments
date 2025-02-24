from dataclasses import dataclass
from datetime import datetime
from seedwork.dominio.eventos import EventoDominio

@dataclass
class ImagenSubida(EventoDominio):
    id: str
    nombre: str
    formato: str
    fecha_subida: datetime

@dataclass
class ImagenProcesada(EventoDominio):
    id: str
    url: str
    fecha_procesamiento: datetime
