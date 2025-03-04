from dataclasses import dataclass

from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.entidades import Entidad

from .entidades import SolicitudDescarga
from .reglas import ValidarFormatoDescarga
from .excepciones import TipoObjetoNoExisteEnDominioStandardExcepcion

@dataclass
class _FabricaSolicitudDescarga(Fabrica):
  def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
    if isinstance(obj, Entidad):
      return mapeador.entidad_a_dto(obj)
    else:
      solicitud_descarga: SolicitudDescarga = mapeador.dto_a_entidad(obj)
      
      [self.validar_regla(ValidarFormatoDescarga(img.formato)) for img in solicitud_descarga.imagenes]

      return solicitud_descarga
    
@dataclass
class FabricaSolicitudDescarga(Fabrica):
  def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
    if mapeador.obtener_tipo() == SolicitudDescarga.__class__:
      fabrica_solicitud_descarga = _FabricaSolicitudDescarga()
      return fabrica_solicitud_descarga.crear_objeto(obj, mapeador)
    else:
      raise TipoObjetoNoExisteEnDominioStandardExcepcion()