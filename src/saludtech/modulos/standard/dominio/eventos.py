from dataclasses import dataclass
from datetime import datetime
import uuid

from saludtech.seedwork.dominio.eventos import EventoDominio

class EventoSolicitud(EventoDominio):
  ...
  
@dataclass
class SolicitudDescargaCreada(EventoSolicitud):
  id_solicitud: uuid.UUID = None
  id_usuario: uuid.UUID = None
  estado_descarga: str = None
  fecha_creacion: datetime = None

@dataclass
class SolicitudDescargaFallida(EventoSolicitud):
  id_solicitud: uuid.UUID = None
  id_usuario: uuid.UUID = None
  estado_descarga: str = None
  fecha_creacion: datetime = None

@dataclass
class PaqueteGenerado(EventoSolicitud):
  ...
@dataclass
class GenerarPaqueteFallido(EventoSolicitud):
  ...

@dataclass
class NotificacionGenerada(EventoSolicitud):
  ...
@dataclass
class NotificarUsuarioFallido(EventoSolicitud):
  