from saludtech.seedwork.dominio.repositorios import Mapeador

from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from saludtech.modulos.standard.infraestructura.dto import SolicitudDescargaV1 as SolicitudDescargaDTO
from saludtech.modulos.standard.dominio.eventos import SolicitudDescargaCreada, EventoSolicitud
from saludtech.seedwork.infraestructura.utils import unix_time_millis


class MapeadorSolicitudDescarga(Mapeador):

  def obtener_tipo(self):
    return SolicitudDescarga.__class__
  
  def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
    solicitud_descarga = SolicitudDescarga(
      fecha_creacion=dto.fecha_creacion,
      fecha_actualizacion=dto.fecha_actualizacion,
      id=dto.id,
      usuario_id=dto.usuario_id,
      estado_descarga=dto.estado
    )
    
    return solicitud_descarga
  
  def entidad_a_dto(self, entidad: SolicitudDescarga) -> SolicitudDescargaDTO:
    
    solicitud_descarga_dto = SolicitudDescargaDTO(
      fecha_creacion=entidad.fecha_creacion,
      fecha_actualizacion=entidad.fecha_actualizacion,
      id=str(entidad.id),
      usuario_id=str(entidad.id_usuario),
      estado=entidad.estado_descarga.value
    )
    
    return solicitud_descarga_dto


class MapeadorEventoSolicitudDescarga(Mapeador):
  ...
  versions = ('v1',)
  
  LATEST_VERSION = versions[0]
  
  def __init__(self):
    self.router = {
      SolicitudDescargaCreada: self._entidad_a_solicitud_creada
    }
  
  def obtener_tipo(self) -> type:
    return EventoSolicitud.__class__

  def es_version_valida(self, version):
      for v in self.versions:
          if v == version:
              return True
      return False
    
  def _entidad_a_solicitud_creada(self, entidad: SolicitudDescargaCreada, version= LATEST_VERSION):
    def v1(evento):
      from .schema.v1.eventos import SolicitudCreadaPayload, EventoSolicitudCreada
      
      payload = SolicitudCreadaPayload(
        id=str(evento.id),
        usuario_id=str(evento.usuario_id),
        formato=evento.formato,
        fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
      )
      
      evento_integracion = EventoSolicitudCreada(id=str(evento.id))
      evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
      evento_integracion.specversion = str(version)
      evento_integracion.type = 'SolicitudDescargaCreada'
      evento_integracion.datacontenttype = 'AVRO'
      evento_integracion.service_name = 'saludtech'
      evento_integracion.data = payload
      
      return evento_integracion

    if not self.es_version_valida(version):
      raise Exception(f'No se sabe procesar la version {version}')

    if version == 'v1':
      return v1(entidad)       