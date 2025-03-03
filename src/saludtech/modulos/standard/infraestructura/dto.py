
from saludtech.config.db import db


Base = db.declarative_base()

class SolicitudDescarga(db.Model):
  __tablename__ = 'solicitudes_descarga'
  id = db.Column(db.String, primary_key=True)
  usuario_id = db.Column(db.String)
  formato = db.Column(db.String)
  estado = db.Column(db.String)
  fecha_creacion = db.Column(db.DateTime)
  fecha_actualizacion = db.Column(db.DateTime)