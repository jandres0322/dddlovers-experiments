from saludtech.modules.gestion_descargas.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.modules.gestion_descargas.dominio.fabricas import FabricaSolicitudDescarga
from saludtech.modules.gestion_descargas.dominio.entidades import SolicitudDescarga
from saludtech.config.db import db
from .mapeadores import MapeadorSolicitudDescarga

class RepositorioSolicitudSQLAlchemy(RepositorioSolicitudDescarga):
    
    def __init__(self):
        self.fabrica_reserva: FabricaSolicitudDescarga = FabricaSolicitudDescarga()
        
    def agregar(self, entidad: SolicitudDescarga):
        solicitud_dto = self.fabrica_reserva.crear_objeto(entidad, MapeadorSolicitudDescarga())
        db.session.add(solicitud_dto)
        
    def obtener_por_id(self, id):
        return super().obtener_por_id(id)
    
    def obtener_todos(self):
        return super().obtener_todos()
    
    def actualizar(self, entity):
        return super().actualizar(entity)
    
    def eliminar(self, entity_id):
        return super().eliminar(entity_id)