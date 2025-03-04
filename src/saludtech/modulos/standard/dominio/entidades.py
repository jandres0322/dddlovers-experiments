from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID 

from saludtech.seedwork.dominio.entidades import AgregacionRaiz, Entidad

from .objetos_valor import EstadoDescarga, FormatoArchivo
from .eventos import SolicitudDescargaCreada

@dataclass
class ImagenMedica(Entidad):
  formato: FormatoArchivo = field(default_factory=FormatoArchivo)
  ubicacion: str = field(default_factory=str)

@dataclass
class SolicitudDescarga(AgregacionRaiz):
  id_usuario: UUID = field(hash=True, default=None)
  estado_descarga: EstadoDescarga = field(default=EstadoDescarga.PENDIENTE)
  imagenes: list[ImagenMedica] = field(default_factory=list)
  
  def crear_solicitud(self, solicitud: SolicitudDescarga):
    self.id_usuario = solicitud.id_usuario
    self.estado_descarga = solicitud.estado_descarga
    self.imagenes = solicitud.imagenes
    self.fecha_creacion = datetime.now()
    
    self.agregar_evento(SolicitudDescargaCreada(
      id_solicitud=self.id,
      id_usuario=self.id_usuario,
      estado_descarga=self.estado_descarga.name,
      fecha_creacion=self.fecha_creacion
    ))