from saludtech.seedwork.aplicacion.dto import DTO
from dataclasses import field, dataclass

@dataclass(frozen=True)
class SolicitudDescargaDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_modificacion: str = field(default_factory=str)
    id_usuario: str = field(default_factory=str)
    imagenes: list[str] = field(default_factory=list)
    formato: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    