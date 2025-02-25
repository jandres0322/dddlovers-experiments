from saludtech.seedwork.aplicacion.comandos import Comando, ComandoHandler
from saludtech.modulos.imagenes.dominio.servicios import ServicioEntregaImagen
from saludtech.modulos.imagenes.aplicacion.dto import EntregaImagenDTO
from saludtech.modulos.imagenes.aplicacion.mapeadores import MapeadorEntregaImagen
from dataclasses import dataclass

@dataclass
class MarcarDisponible(Comando):
    entrega: EntregaImagenDTO

class MarcarDisponibleHandler(ComandoHandler):

    def __init__(self, servicio: ServicioEntregaImagen, mapeador: MapeadorEntregaImagen):
        self.servicio = servicio
        self.mapeador = mapeador

    def handle(self, comando: MarcarDisponible):
        entrega = self.mapeador.dto_a_externo(comando.entrega)        
        self.servicio.marcar_como_disponible(entrega.id)
