from saludtech.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
import uuid


@dataclass
class EventoPaqueteDescargaGenerado(EventoDominio):
    id_solicitud: uuid.UUID = None
    ruta_zip: str = None