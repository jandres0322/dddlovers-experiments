from dataclasses import dataclass

from saludtech.seedwork.aplicacion.comandos import Comando, ejecutar_commando as comando

from saludtech.modulos.standard.aplicacion.dto import ImagenMedicaDTO, SolicitudDescargaDTO
from saludtech.modulos.standard.aplicacion.mapeadores import MapeadorSolicitudDescarga
from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from saludtech.modulos.standard.dominio.repositorios import RepositorioSolicitudDescarga

from .base import SolicitarDescargaBaseHandler

@dataclass
class ComandoSolicitarDescarga(Comando):
  fecha_creacion: str
  fecha_actualizacion: str
  id: str
  usuario_id: str
  imagenes: list[ImagenMedicaDTO]
  
class SolicitarDescargaHandler(SolicitarDescargaBaseHandler):

  def handle(self, comando: ComandoSolicitarDescarga):
    solicitud_dto = SolicitudDescargaDTO(
      fecha_actualizacion=comando.fecha_actualizacion,
      fecha_creacion=comando.fecha_creacion,
      id=comando.id,
      usuario_id=comando.usuario_id,
      imagenes=comando.imagenes
    )

    solicitud: SolicitudDescarga = self.fabrica_solicitud_descarga.crear_objeto(solicitud_dto, MapeadorSolicitudDescarga() )
    solicitud.crear_solicitud(solicitud)
    
    repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSolicitudDescarga)
  
    repositorio.agregar(solicitud)
    
    pass
  
  
@comando.register(ComandoSolicitarDescarga)
def ejecutar_comando_solicitar_descarga(comando: ComandoSolicitarDescarga):
  handler = SolicitarDescargaHandler()
  handler.handle(comando)