from __future__ import annotations
from saludtech.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass, field
import uuid
from datetime import datetime

class EventoSolicitud(EventoDominio):
    ...
    
@dataclass
class EventoSolicitudDescargaCreada(EventoSolicitud):
    id: uuid.UUID = None
    id_usuario: uuid.UUID = None
    id_solicitud: uuid.UUID = None
    id_imagenes: str = None
