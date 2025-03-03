from dataclasses import dataclass

from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.entidades import Entidad

from .entidades import SolicitudDescarga
from .excepciones import TipoObjetoNoExisteEnDominioStandardExcepcion
from .reglas import FormatoDescargaValido

@dataclass
class _FabricaSolicitudDescarga(Fabrica):
  
  def crear_objeto(self, obj, mapeador: Mapeador):
    if isinstance(obj, Entidad):
      return mapeador.entidad_a_dto(obj)
    else:
      solicitud_descarga: SolicitudDescarga = mapeador.dto_a_entidad(obj)
      self.validar_regla(FormatoDescargaValido(solicitud_descarga.formato))
      
      return solicitud_descarga
    
@dataclass
class FabricaSolicitudDescarga(Fabrica):
  
  def crear_objeto(self, obj, mapeador: Mapeador):
    if mapeador.obtener_tipo() == SolicitudDescarga.__class__:
      fabrica_solicitud_descarga = _FabricaSolicitudDescarga()
      return fabrica_solicitud_descarga.crear_objeto(obj, mapeador)
    else:
      raise TipoObjetoNoExisteEnDominioStandardExcepcion()