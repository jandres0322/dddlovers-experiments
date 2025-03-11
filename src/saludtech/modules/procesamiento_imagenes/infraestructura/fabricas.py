from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.modules.procesamiento_imagenes.dominio.repositorios import RepositorioImagenesProcesada
from saludtech.modules.procesamiento_imagenes.infraestructura.mapeadores import MapeadorImagenMedica
from .repositorios import RepositorioImagenesSQLAlchemy
from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):

    def crear_objeto(self, obj, mapeador = None):
        if obj == RepositorioImagenesProcesada:
            return RepositorioImagenesSQLAlchemy()
        else:
            raise ExcepcionFabrica("No se puede crear un repositorio")
        

