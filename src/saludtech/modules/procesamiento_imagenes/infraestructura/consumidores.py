import logging
import traceback
import pulsar
from pulsar.schema import AvroSchema
from saludtech.modules.procesamiento_imagenes.infraestructura.schemas.v1.eventos import EventoSolicitudCreada
from saludtech.seedwork.aplicacion.queries import ejecutar_query
from saludtech.modules.procesamiento_imagenes.aplicacion.mapeadores import MapeadorObtenerImagenesDTOJson
from saludtech.modules.procesamiento_imagenes.aplicacion.queries.obtener_imagenes import ObtenerImagenes

def subscribirse_a_eventos(app=None):
    print('subscribirse_a_eventos')
    cliente = None
    try:
        cliente = pulsar.Client('pulsar://broker:6650')
        consumer = cliente.subscribe(
            'eventos-solicitud-descarga-creada',
            subscription_name='sub-procesamiento-imagenes-eventos-solicitud-descarga',
            schema=AvroSchema(EventoSolicitudCreada)
        )
        
        while True:
            mensaje = consumer.receive()
            datos = mensaje.value().data
            
            print('datos', datos)
            
            map_obtener_imagenes = MapeadorObtenerImagenesDTOJson()
            obtener_imagen_dto = map_obtener_imagenes.externo_a_dto(datos)
                        
            
            query_resultado = ejecutar_query(ObtenerImagenes(
                id_solicitud = obtener_imagen_dto.id_solicitud,
                id_imagenes= obtener_imagen_dto.id_imagenes
            ))

            return map_obtener_imagenes.dto_a_externo(query_resultado.resultado)
            
            consumer.acknowledge(mensaje)
            
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()