from uuid import UUID
from saludtech.seedwork.dominio.repositorios import Repositorio
from typing import Optional, List
from saludtech.modulos.usuarios.infraestructura.dto import UsuarioORM
from saludtech.config.db import db

class RepositorioUsuarioSQL(Repositorio):

    def obtener_por_id(self, id: UUID) -> Optional[UsuarioORM]:
        return UsuarioORM.query.get(id)

    def obtener_todos(self) -> List[UsuarioORM]:
        raise NotImplementedError

    def agregar(self, entity: UsuarioORM):
        db.session.add(entity)
        db.session.commit()
        return entity

    def actualizar(self, entity: UsuarioORM):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError