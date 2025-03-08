from __future__ import annotations
from saludtech.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
import uuid

class EventoSolicitud(EventoDominio):
    ...
    
@dataclass
class SolicitudDescargaCreada(EventoSolicitud):
    id_usuario: uuid.UUID
    imagenes: list[str]
    formato: str
    estado: str
