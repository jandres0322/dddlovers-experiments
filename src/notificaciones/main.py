import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class SolicitudCreadaPayload(Record):
    id_solicitud = String()
    id_usuario = String()
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

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client('pulsar://broker:6650')

consumer = client.subscribe(
    'eventos-solicitud-descarga-creada',  # 👈 Tópico corregido
    subscription_name='sub-notificacion-eventos-reservas',
    schema=AvroSchema(EventoSolicitudCreada)
)

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()