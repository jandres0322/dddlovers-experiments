from __future__ import annotations
from saludtech.seedwork.dominio.entidades import AgregacionRaiz
from dataclasses import dataclass, field
from .objetos_valor import EstadoDescarga, FormatoDescarga
from .eventos import EventoSolicitudDescargaCreada
from datetime import datetime

@dataclass
class SolicitudDescarga(AgregacionRaiz):
    id_usuario: str = field(default_factory=str)
    imagenes: list[str] = field(default_factory=list)
    formato: FormatoDescarga = field(default=FormatoDescarga.DICOM)
    estado: EstadoDescarga = field(default=EstadoDescarga.PENDIENTE)
    
    def crear_solicitud(self, solicitud: SolicitudDescarga):
        self.id_usuario = solicitud.id_usuario
        self.imagenes = solicitud.imagenes
        self.formato = solicitud.formato
        self.estado = solicitud.estado
        self.fecha_creacion = datetime.now()
        
        self.agregar_evento(
            EventoSolicitudDescargaCreada(
                id=self.id,
                id_usuario=self.id_usuario,
                id_solicitud=solicitud.id,
                id_imagenes=solicitud.imagenes
            )
        )

    def cambiar_estado(self, estado: EstadoDescarga):
        self.estado = estado
        self.fecha_actualizacion = datetime.now()