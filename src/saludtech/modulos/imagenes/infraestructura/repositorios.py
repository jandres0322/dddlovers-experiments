from saludtech.modulos.imagenes.dominio.repositorios import RepositorioEntregaImagen, RepositorioHistorialEntrega
from saludtech.config.db import db
from saludtech.modulos.imagenes.infraestructura.dto import EntregaImagenORM, HistorialEntregaORM
import uuid

class RepositorioEntregaImagenSQLAlchemy(RepositorioEntregaImagen):
    """Repositorio para la persistencia de la entidad EntregaImagen."""

    def obtener_por_id(self, id_entrega: uuid.UUID) -> EntregaImagenORM:
        """Obtiene una entrega de imagen por su ID."""
        return EntregaImagenORM.query.get(id_entrega)

    def obtener_todos(self) -> list[EntregaImagenORM]:
        """Obtiene todas las entregas de imágenes almacenadas."""
        return EntregaImagenORM.query.all()

    def agregar(self, entrega: EntregaImagenORM):
        """Agrega una nueva entrega de imagen a la base de datos."""
        db.session.add(entrega)
        db.session.commit()

    def actualizar(self, entrega: EntregaImagenORM):
        """Actualiza una entrega de imagen existente en la base de datos."""
        db.session.merge(entrega)
        db.session.commit()

    def eliminar(self, id_entrega: uuid.UUID):
        """Elimina una entrega de imagen de la base de datos."""
        entrega = self.obtener_por_id(id_entrega)
        if entrega:
            db.session.delete(entrega)
            db.session.commit()

class RepositorioHistorialEntrega(RepositorioHistorialEntrega):
    """Repositorio para la persistencia del historial de descargas."""

    def obtener_por_id(self, id_historial: uuid.UUID) -> HistorialEntregaORM:
        """Obtiene el historial de descargas por su ID."""
        return HistorialEntregaORM.query.get(id_historial)

    def obtener_todos(self) -> list[HistorialEntregaORM]:
        """Obtiene todos los registros de descargas almacenados."""
        return HistorialEntregaORM.query.all()

    def agregar(self, historial: HistorialEntregaORM):
        """Agrega un nuevo historial de descargas a la base de datos."""
        db.session.add(historial)
        db.session.commit()

    def actualizar(self, historial: HistorialEntregaORM):
        """Actualiza un historial de descargas existente en la base de datos."""
        db.session.merge(historial)
        db.session.commit()

    def eliminar(self, id_historial: uuid.UUID):
        """Elimina un historial de descargas de la base de datos."""
        historial = self.obtener_por_id(id_historial)
        if historial:
            db.session.delete(historial)
            db.session.commit()

