from uuid import UUID
from typing import Optional, List
from seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.imagenes.dominio.entidades import EntregaImagen, HistorialEntrega

class RepositorioEntregaImagen(Repositorio):

    def obtener_por_id(self, id: UUID) -> Optional[EntregaImagen]:
        raise NotImplementedError

    def obtener_todos(self) -> List[EntregaImagen]:
        raise NotImplementedError

    def agregar(self, entity: EntregaImagen):
        raise NotImplementedError

    def actualizar(self, entity: EntregaImagen):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError

class RepositorioHistorialEntrega(Repositorio):

    def obtener_por_id(self, id: UUID) -> Optional[HistorialEntrega]:
        raise NotImplementedError

    def obtener_todos(self) -> List[HistorialEntrega]:
        raise NotImplementedError

    def agregar(self, entity: HistorialEntrega):
        raise NotImplementedError

    def actualizar(self, entity: HistorialEntrega):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError
