from pulsar.schema import Record, String, Long
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from saludtech.seedwork.infraestructura.utils import time_millis
import uuid

class SolicitudCreadaPayload(Record):
    id_solicitud = String()
    id_usuario = String()
    estado = String()
    fecha_creacion = Long()
    
class EventoSolicitudCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = SolicitudCreadaPayload()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    