from saludtech.config.db import db


class ImagenProcesada(db.Model):
    __tablename___ = "imagenes_medicas",
    id = db.Column(db.String, primary_key=True)
    ruta_storage = db.Column(db.String)
    ruta_thumbanil = db.Column(db.String)
    ruta_metadatos = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
