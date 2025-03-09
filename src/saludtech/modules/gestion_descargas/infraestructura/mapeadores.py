from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modules.gestion_descargas.dominio.entidades import SolicitudDescarga
from saludtech.modules.gestion_descargas.dominio.eventos import EventoSolicitudDescargaCreada, EventoSolicitud
from .dto import SolicitudDescarga as SolicitudDescargaDTO
from datetime import datetime
from saludtech.seedwork.infraestructura.utils import unix_time_millis
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

class MapeadorEventoSolicitudDesarga(Mapeador):
    ...
    
    versions = ('v1',)
    
    LATEST_VERSION = versions[0]
    
    def __init__(self):
        self.router = {
            EventoSolicitudDescargaCreada: self._entidad_a_solicitud_creada
        }
        
    def obtener_tipo(self):
        return EventoSolicitudDescargaCreada.__class__
    
    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False
    
    def _entidad_a_solicitud_creada(self, entidad: EventoSolicitudDescargaCreada,  version=LATEST_VERSION):
        def v1(evento):
            print('evento', evento.__dict__)
            from .schema.v1.eventos import SolicitudCreadaPayload, EventoSolicitudCreada
            
            payload = SolicitudCreadaPayload(
                id_solicitud=str(evento.id),
                id_usuario=str(evento.id_usuario),
                estado=evento.estado.value,
            )
            
            evento_integracion = EventoSolicitudCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            # evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'SolicitudDescargaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'saludtech.gestion-descargas'
            evento_integracion.data = payload
            
            return evento_integracion
        
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)
            
    def entidad_a_dto(self, entidad: EventoSolicitud, version=LATEST_VERSION) -> SolicitudDescargaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)
    
    def dto_a_entidad(self, dto):
        return super().dto_a_entidad(dto)


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
