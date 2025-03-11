
from dataclasses import dataclass, field

@dataclass(frozen=True)
class ImagenMedicaDTO:
  fecha_creacion: str = field(default_factory=str)
  fecha_actualizacion: str = field(default_factory=str)
  id: str = field(default_factory=str)
  imagen_id: str = field(default_factory=str)
  formato: str = field(default_factory=str)

@dataclass(frozen=True)
class SolicitudDescargaDTO:
  fecha_creacion: str = field(default_factory=str)
  fecha_actualizacion: str = field(default_factory=str)
  id: str = field(default_factory=str)
  usuario_id: str = field(default_factory=str)
  imagenes: list[ImagenMedicaDTO] = field(default_factory=list)
