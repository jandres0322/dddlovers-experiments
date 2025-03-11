import pulsar
from pulsar.schema import AvroSchema

from saludtech.modules.gestion_descargas.infraestructura.mapeadores import MapeadorEventoSolicitudDesarga
from saludtech.modules.gestion_descargas.infraestructura.schema.v1.eventos import EventoSolicitudCreada

class Despachador:    
    def __init__(self):
        self.mapper = MapeadorEventoSolicitudDesarga()
    
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client("pulsar://broker:6650")
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoSolicitudCreada))
        publicador.send(mensaje)
        cliente.close()
        
    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))
        
    def publicar_comando(self, comando, topico):
        ...
    