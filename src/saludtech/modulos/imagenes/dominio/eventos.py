from dataclasses import dataclass
from datetime import datetime
from seedwork.dominio.eventos import EventoDominio

@dataclass
class ImagenProcesada(EventoDominio):
    id_imagen: str
    fecha_procesamiento: datetime
