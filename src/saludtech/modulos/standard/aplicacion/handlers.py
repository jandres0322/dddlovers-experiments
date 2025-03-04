
from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modulos.standard.infraestructura.despachadores import Despachador

class HandlerSolicitudDescargaIntegracion(Handler):
    
    @staticmethod
    def handle_solicitud_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-solicitud')