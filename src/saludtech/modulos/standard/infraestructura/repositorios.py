
from saludtech.config.db import db

from saludtech.modulos.standard.dominio.repositorios import RepositorioSolicitudDescarga
from saludtech.modulos.standard.dominio.entidades import SolicitudDescarga
from saludtech.modulos.standard.dominio.fabricas import FabricaSolicitudDescarga
from saludtech.modulos.standard.infraestructura.mapeadores import MapeadorSolicitudDescarga

class RepositorioSolicitudDescargaSQLAlchemy(RepositorioSolicitudDescarga):
  
  def __init__(self):
    self._fabrica_solicitud_descarga: FabricaSolicitudDescarga = FabricaSolicitudDescarga()
    
  @property
  def fabrica_solicitud_descarga(self):
    return self._fabrica_solicitud_descarga
    
  def agregar(self, solicitud_descarga: SolicitudDescarga):
    solicitud_descarga_dto = self.fabrica_solicitud_descarga.crear_objeto(solicitud_descarga, MapeadorSolicitudDescarga())
    db.session.add(solicitud_descarga_dto)
    db.session.commit()
    
  def obtener_por_id(self, id: int) -> SolicitudDescarga:
    pass

  def obtener_todos(self):
    return super().obtener_todos()
  
  def actualizar(self, entity):
    return super().actualizar(entity)
  
  def eliminar(self, entity_id):
    return super().eliminar(entity_id)