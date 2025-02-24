from abc import ABC, abstractmethod
from .entidades import ImagenMedica

class RepositorioImagenes(ABC):
    @abstractmethod
    def obtener_por_id(self, id_imagen: str) -> ImagenMedica:
        pass

    @abstractmethod
    def guardar(self, imagen: ImagenMedica) -> None:
        pass

    @abstractmethod
    def listar_procesadas(self) -> list[ImagenMedica]:
        pass
