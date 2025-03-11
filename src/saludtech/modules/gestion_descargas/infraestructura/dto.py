from saludtech.config.db import db

class SolicitudDescarga(db.Model):
    __tablename__ = 'solicitud_descarga'
    
    id = db.Column(db.String(255), primary_key=True)
    id_usuario = db.Column(db.String(255), nullable=False)
    imagenes = db.Column(db.String(255), nullable=False)
    formato = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
