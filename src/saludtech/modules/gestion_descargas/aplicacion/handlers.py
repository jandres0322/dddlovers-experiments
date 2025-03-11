from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modules.gestion_descargas.infraestructura.despachadores import Despachador

class HandlerSolicitudIntegracion(Handler):
    
    @staticmethod
    def handle_solicitud_descarga_creada(evento):
        print('handle solicitud descarga creada')
        despachador = Despachador()
        despachador.publicar_evento(evento, "eventos-solicitud-descarga-creada")