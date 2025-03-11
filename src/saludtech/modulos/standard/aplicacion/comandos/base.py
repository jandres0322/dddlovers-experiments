
from saludtech.seedwork.aplicacion.comandos import ComandoHandler

from saludtech.modulos.standard.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.standard.dominio.fabricas import FabricaSolicitudDescarga

class SolicitarDescargaBaseHandler(ComandoHandler):
  
  def __init__(self):
    self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    self._fabrica_solicitud_descarga: FabricaSolicitudDescarga = FabricaSolicitudDescarga()
    
  @property
  def fabrica_repositorio(self):
    return self._fabrica_repositorio
  
  @property
  def fabrica_solicitud_descarga(self):
    return self._fabrica_solicitud_descarga