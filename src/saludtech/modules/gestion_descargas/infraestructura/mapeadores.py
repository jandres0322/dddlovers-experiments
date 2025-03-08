from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modules.gestion_descargas.dominio.entidades import SolicitudDescarga
from .dto import SolicitudDescarga as SolicitudDescargaDTO
from datetime import datetime

class MapeadorSolicitudDescarga(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    
    def obtener_tipo(self):
        return SolicitudDescarga.__class__
    
    def entidad_a_dto(self, entidad: SolicitudDescarga) -> SolicitudDescargaDTO:
        solicitud_dto = SolicitudDescargaDTO()
        
        solicitud_dto.id = str(entidad.id)
        solicitud_dto.id_usuario = entidad.id_usuario
        solicitud_dto.formato = entidad.formato.value
        solicitud_dto.estado = entidad.estado.value
        solicitud_dto.imagenes = str(entidad.imagenes)
        solicitud_dto.fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        solicitud_dto.fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        
        return solicitud_dto
        
    
    def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
        return SolicitudDescarga(
            id=dto.id,
            id_usuario=dto.id_usuario,
            formato=dto.formato,
            estado=dto.estado,
            fecha_creacion=datetime.strptime(dto.fecha_creacion, self._FORMATO_FECHA),
            fecha_actualizacion=datetime.strptime(dto.fecha_actualizacion, self._FORMATO_FECHA)
        )
