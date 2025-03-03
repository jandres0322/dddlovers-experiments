from saludtech.seedwork.dominio.repositorios import Mapeador

from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from saludtech.modulos.standard.infraestructura.dto import SolicitudDescarga as SolicitudDescargaDTO


class MapeadorSolicitudDescarga(Mapeador):

  def obtener_tipo(self):
    return SolicitudDescarga.__class__
  
  def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
    solicitud_descarga = SolicitudDescarga(
      fecha_creacion=dto.fecha_creacion,
      fecha_actualizacion=dto.fecha_actualizacion,
      id=dto.id,
      usuario_id=dto.usuario_id,
      formato=dto.formato
    )
    
    return solicitud_descarga
  
  def entidad_a_dto(self, entidad: SolicitudDescarga) -> SolicitudDescargaDTO:
    
    solicitud_descarga_dto = SolicitudDescargaDTO(
      fecha_creacion=entidad.fecha_creacion,
      fecha_actualizacion=entidad.fecha_actualizacion,
      id=str(entidad.id),
      usuario_id=str(entidad.usuario_id),
      formato=entidad.formato,
      estado=entidad.estado.value
    )
    
    return solicitud_descarga_dto
  