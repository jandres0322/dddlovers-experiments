from dataclasses import dataclass

from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

from saludtech.modulos.standard.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.modulos.standard.infraestructura.repositorios import RepositorioSolicitudDescargaSQLAlchemy

@dataclass
class FabricaRepositorio(Fabrica):
  
  def crear_objeto(self, obj, mapeador = None) -> Repositorio:
    if obj == RepositorioSolicitudDescarga:
      print('crear_objeto')
      return RepositorioSolicitudDescargaSQLAlchemy()
    else:
      raise ExcepcionFabrica('No se puede crear el objeto solicitado')