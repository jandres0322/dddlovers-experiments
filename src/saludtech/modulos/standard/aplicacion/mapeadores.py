
from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap

from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from saludtech.modulos.standard.dominio.objetos_valor import FormatoDescarga

from .dto import SolicitudDescargaDTO

class MapeadorSolicitudDescargaDTOJson(AppMap):

  def externo_a_dto(self, externo:dict) -> SolicitudDescargaDTO:
    solicitud_descarga_dto = SolicitudDescargaDTO(
      usuario_id=externo.get('usuario_id'),
      formato=externo.get('formato')
    )
    
    return solicitud_descarga_dto
    
  
  def dto_a_externo(self, dto):
    return dto.__dict__


class MapeadorSolicitudDescarga(RepMap):  
  _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

  
  def obtener_tipo(self):
    return SolicitudDescarga.__class__
  
  def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
    formato = FormatoDescarga(valor=dto.formato)
    solicitud_descarga = SolicitudDescarga(formato=formato)
    solicitud_descarga.usuario_id = dto.usuario_id
    solicitud_descarga.formato = dto.formato
    
    return solicitud_descarga
  
  def entidad_a_dto(self, entidad: SolicitudDescarga) -> SolicitudDescargaDTO:
    fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
    fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
    _id = str(entidad.id)
    
    return SolicitudDescargaDTO(
      fecha_creacion=fecha_creacion,
      fecha_actualizacion=fecha_actualizacion,
      id=_id,
      usuario_id=entidad.usuario_id,
      formato=entidad.formato,
      estado=entidad.estado.value
    )