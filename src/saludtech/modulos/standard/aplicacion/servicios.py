
from saludtech.seedwork.aplicacion.servicios import Servicio

from saludtech.modulos.standard.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.standard.dominio.fabricas import FabricaSolicitudDescarga
from saludtech.modulos.standard.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from .dto import SolicitudDescargaDTO
from .mapeadores import MapeadorSolicitudDescarga

class ServicioSolicitudDescarga(Servicio):
  
  def __init__(self):
    self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    self._fabrica_solicitud_descarga: FabricaSolicitudDescarga = FabricaSolicitudDescarga()
    
  @property
  def fabrica_repositorio(self):
    return self._fabrica_repositorio
  
  @property
  def fabrica_solicitud_descarga(self):
    return self._fabrica_solicitud_descarga
  
  def solicitar_descarga(self, solicitud_descarga_dto: SolicitudDescargaDTO) -> SolicitudDescargaDTO:
    solicitud_descarga: SolicitudDescarga = self.fabrica_solicitud_descarga.crear_objeto(solicitud_descarga_dto, MapeadorSolicitudDescarga())

    repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSolicitudDescarga.__class__)
    repositorio.agregar(solicitud_descarga)
    
    return self.fabrica_solicitud_descarga.crear_objeto(solicitud_descarga, MapeadorSolicitudDescarga())