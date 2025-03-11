from saludtech.modules.procesamiento_imagenes.dominio.repositorios import RepositorioImagenesProcesada
from saludtech.modules.procesamiento_imagenes.dominio.fabricas import FabricaImagenProcesada
from saludtech.modules.procesamiento_imagenes.dominio.entidades import ImagenProcesada
from saludtech.config.db import db
from .dto import ImagenProcesada as ImagenProcesadaDTO
from .mapeadores import MapeadorImagenMedica

class RepositorioImagenesSQLAlchemy(RepositorioImagenesProcesada):
    
    def __init__(self):
        self.fabrica_imagenes: FabricaImagenProcesada = FabricaImagenProcesada()

    def obtener_por_id(self, id) -> ImagenProcesada:
        imagen_dto = db.session.query(ImagenProcesadaDTO).filter_by(id=str(id)).one_or_none()
        return self.fabrica_imagenes.crear_objeto(imagen_dto, MapeadorImagenMedica)
    
    def obtener_todos(self):
        return super().obtener_todos()
    
    def actualizar(self, entity):
        return super().actualizar(entity)
    
    def agregar(self, entity):
        return super().agregar(entity)
    
    def eliminar(self, entity_id):
        return super().eliminar(entity_id)
