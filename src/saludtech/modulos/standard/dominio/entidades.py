
from dataclasses import dataclass, field

from saludtech.seedwork.dominio.entidades import AgregacionRaiz

import saludtech.modulos.standard.dominio.objetos_valor as ov

@dataclass
class SolicitudDescarga(AgregacionRaiz):
  usuario_id: str = field(default_factory=str)
  formato: ov.FormatoDescarga = field(default_factory=ov.FormatoDescarga)
  estado: ov.EstadoSolicitud = field(default=ov.EstadoSolicitud.PENDIENTE)
  
  def cambiar_estado(self, nuevo_estado: ov.EstadoSolicitud):
    self.estado = nuevo_estado
    
  def es_procesable(self) -> bool:
    return self.estado == ov.EstadoSolicitud.PENDIENTE