
from saludtech.config.db import db
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from saludtech.modulos.standard.dominio.objetos_valor import EstadoDescarga, FormatoArchivo

Base = db.declarative_base()

class SolicitudDescargaV1(db.Model):
    __tablename__ = 'solicitudes_descarga_v1'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    usuario_id = Column(String, nullable=False)
    estado = Column(Enum(EstadoDescarga), nullable=False, default=EstadoDescarga.PENDIENTE)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, onupdate=datetime.utcnow)
    
    # Relación con las imágenes médicas
    imagenes = relationship('ImagenMedica', back_populates='solicitud', cascade="all, delete-orphan")

class ImagenMedica(db.Model):
    __tablename__ = 'imagenes_medicas'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    solicitud_id = Column(String, ForeignKey('solicitudes_descarga_v1.id'), nullable=False)
    formato = Column(Enum(FormatoArchivo), nullable=False)
    ubicacion = Column(String, nullable=False)

    solicitud = relationship('SolicitudDescargaV1', back_populates='imagenes')