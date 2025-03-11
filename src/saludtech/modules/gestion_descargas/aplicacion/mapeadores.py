from saludtech.seedwork.aplicacion.dto import Mapeador as AppMapper
from saludtech.seedwork.dominio.repositorios import Mapeador as RepoMapper

from .dto import SolicitudDescargaDTO
from saludtech.modules.gestion_descargas.dominio.entidades import SolicitudDescarga
from saludtech.modules.gestion_descargas.dominio.objetos_valor import FormatoDescarga


class MapeadorSolicitudDTOJson(AppMapper):
    
    def externo_a_dto(self, externo: dict) -> SolicitudDescargaDTO:
        
        solicitud_dto = SolicitudDescargaDTO(
            id_usuario=externo['id_usuario'],
            imagenes=externo['imagenes'],
            formato=externo['formato'],
        )
        
        return solicitud_dto
        
    def dto_a_externo(self, dto):
        return super().dto_a_externo(dto)
    
    
class MapeadorSolicitudDescarga(RepoMapper):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    
    def obtener_tipo(self):
        return SolicitudDescarga.__class__
    
    def entidad_a_dto(self, solicitud: SolicitudDescarga) -> SolicitudDescargaDTO:
        return SolicitudDescargaDTO(
            id_usuario=solicitud.id_usuario,
            imagenes=solicitud.imagenes,
            formato=solicitud.formato,
            estado=solicitud.estado,
            fecha_creacion=solicitud.fecha_creacion.strftime(self._FORMATO_FECHA),
            fecha_modificacion=solicitud.fecha_actualizacion.strftime(self._FORMATO_FECHA),
            id=solicitud.id
        )
    
    def dto_a_entidad(self, dto: SolicitudDescargaDTO) -> SolicitudDescarga:
        solicitud = SolicitudDescarga()
        solicitud.imagenes = dto.imagenes
        solicitud.id_usuario = dto.id_usuario
        solicitud.formato = FormatoDescarga[dto.formato]
        return solicitud
