from pydispatch import dispatcher

from .handlers import HandlerSolicitudDescargaIntegracion

from saludtech.modulos.standard.dominio.eventos import SolicitudDescargaCreada


dispatcher.connect(HandlerSolicitudDescargaIntegracion.handle_solicitud_creada, signal=f'{SolicitudDescargaCreada.__name__}Integracion' )