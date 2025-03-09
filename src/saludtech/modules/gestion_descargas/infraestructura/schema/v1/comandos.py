from pulsar.schema import String
from saludtech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoSolicitudDescargaPayload(ComandoIntegracion):
    id_usuario = String()
    id_solicitud = String()
    
class ComandoSolicitudDescarga(ComandoIntegracion):
    data = ComandoSolicitudDescargaPayload()