from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio

from saludtech.modules.gestion_descargas.dominio.repositorios import RepositorioSolicitudDescarga
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion
from .repositorios import RepositorioSolicitudSQLAlchemy


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj, mapeador = None) -> Repositorio:
        if obj == RepositorioSolicitudDescarga:
            return RepositorioSolicitudSQLAlchemy()
        else:
            raise NoExisteImplementacionParaTipoFabricaExcepcion()
