from __future__ import annotations
from saludtech.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
import uuid

class EventoSolicitud(EventoDominio):
    ...
    
@dataclass
class EventoSolicitudDescargaCreada(EventoSolicitud):
    id: uuid.UUID = None
    id_usuario: uuid.UUID = None
    formato: str = None
    estado: str = None
