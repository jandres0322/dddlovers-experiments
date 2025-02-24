from uuid import UUID
from typing import Optional, List
from seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.imagenes.dominio.entidades import ImagenMedica

class RepositorioImagenes(Repositorio):

    def obtener_por_id(self, id: UUID) -> Optional[ImagenMedica]:
        raise NotImplementedError

    def obtener_todos(self) -> List[ImagenMedica]:
        raise NotImplementedError

    def agregar(self, entity: ImagenMedica):
        raise NotImplementedError

    def actualizar(self, entity: ImagenMedica):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError
