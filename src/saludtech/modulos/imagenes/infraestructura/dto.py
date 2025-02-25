from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import saludtech.modulos.imagenes.dominio.objetos_valor as ov
from saludtech.config.db import db

class EntregaImagenORM(db.Model):
    __tablename__ = "entregas_imagenes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    imagen_id = Column(String(36))
    usuario_id = Column(String(36))
    estado = Column(Enum(ov.EstadoEntrega), nullable=False, default=ov.EstadoEntrega.DISPONIBLE)
    url_descarga = Column(String, nullable=True)
    fecha_disponible = Column(DateTime, default=datetime.utcnow)

class HistorialEntregaORM(db.Model):
    __tablename__ = "historial_descargas"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    entrega_id = Column(String(36), ForeignKey("entregas_imagenes.id"), nullable=False)
    usuario_id = Column(String(36))
    fecha_descarga = Column(DateTime, default=datetime.utcnow)

    entrega = relationship("EntregaImagenORM", backref="historial_descargas")
