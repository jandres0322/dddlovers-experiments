from dataclasses import dataclass

from saludtech.seedwork.aplicacion.comandos import Comando, ComandoHandler,  ejecutar_commando as comando
from saludtech.modules.gestion_descargas.aplicacion.dto import SolicitudDescargaDTO
from saludtech.modules.gestion_descargas.dominio.fabricas import FabricaSolicitudDescarga
from saludtech.modules.gestion_descargas.dominio.entidades import SolicitudDescarga
from saludtech.modules.gestion_descargas.aplicacion.mapeadores import MapeadorSolicitudDescarga
from saludtech.modules.gestion_descargas.infraestructura.fabricas import FabricaRepositorio
from saludtech.modules.gestion_descargas.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto


@dataclass
class ComandoSolicitarDescarga(Comando):
    id_usuario: str 
    imagenes: list[str]
    formato: str
    estado: str

class SolicitarDescargaHandler(ComandoHandler):
    
    def __init__(self):
        self.fabrica_solicitud = FabricaSolicitudDescarga()
        self.fabrica_repositorio = FabricaRepositorio()
    
    def handle(self, comando: ComandoSolicitarDescarga):
        solicitud_dto = SolicitudDescargaDTO(
            id_usuario=comando.id_usuario,
            imagenes=comando.imagenes,
            formato=comando.formato,
        )
        
        solicitud: SolicitudDescarga = self.fabrica_solicitud.crear_objeto(solicitud_dto, MapeadorSolicitudDescarga())
        solicitud.crear_solicitud(solicitud)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSolicitudDescarga)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, solicitud)
        UnidadTrabajoPuerto.commit()

    
@comando.register(ComandoSolicitarDescarga)
def ejecutar_comando_solicitar_descarga(comando: ComandoSolicitarDescarga):
    handler = SolicitarDescargaHandler()
    handler.handle(comando)