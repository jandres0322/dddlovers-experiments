from abc import ABC

from saludtech.seedwork.dominio.repositorios import Repositorio


class RepositorioSolicitudDescarga(Repositorio, ABC):
  ...
  
class RepositorioEventosSolicitudDescarga(Repositorio, ABC):
  ...