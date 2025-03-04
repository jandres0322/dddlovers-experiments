from saludtech.seedwork.aplicacion.comandos import Comando, ComandoHandler
from saludtech.modulos.imagenes.dominio.servicios import ServicioRegistroDescarga
from saludtech.modulos.imagenes.aplicacion.dto import RegistroDescargaDTO
from saludtech.modulos.imagenes.aplicacion.dto import MapeadorHistorialEntrega
from dataclasses import dataclass


@dataclass
class RegistrarDescarga(Comando):
    registro_descarga: RegistroDescargaDTO

class RegistrarDescargaHandler(ComandoHandler):

    def __init__(self, servicio: ServicioRegistroDescarga, mapeador: MapeadorHistorialEntrega):
        self.servicio = servicio
        self.mapeador = mapeador

    def handle(self, comando: RegistrarDescarga):
        registro = comando.registro_descarga
        self.servicio.registrar_descarga(registro.id_entrega, registro.usuario_id)