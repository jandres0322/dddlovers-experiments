from uuid import UUID
from saludtech.seedwork.dominio.repositorios import Repositorio
from typing import Optional, List
from saludtech.modulos.usuarios.dominio.entidades import Usuario

class RepositorioUsuario(Repositorio):

    def obtener_por_id(self, id: UUID) -> Optional[Usuario]:
        return Usuario.query.get(id)

    def obtener_todos(self) -> List[Usuario]:
        raise NotImplementedError

    def agregar(self, entity: Usuario):
        raise NotImplementedError

    def actualizar(self, entity: Usuario):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError