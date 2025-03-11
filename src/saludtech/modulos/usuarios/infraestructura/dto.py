import uuid
from sqlalchemy.dialects.postgresql import UUID
from saludtech.config.db import db

class UsuarioORM(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)