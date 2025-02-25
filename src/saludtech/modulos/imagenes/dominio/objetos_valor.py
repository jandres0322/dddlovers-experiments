from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class EstadoEntrega(Enum):
    """Estados posibles para la entrega de imágenes procesadas."""
    DISPONIBLE = "DISPONIBLE"
    EXPIRADA = "EXPIRADA"
    ERROR = "ERROR"

@dataclass(frozen=True)
class DatosEntrega:
    """Objeto de valor que encapsula los datos de entrega de una imagen procesada, con autorización."""
    url_descarga: str
    fecha_disponible: datetime
    estado: EstadoEntrega
    autorizado: bool
    
@dataclass(frozen=True)
class RegistroDescarga:
    """Objeto de valor que encapsula la información de una descarga de imagen procesada."""
    usuario_id: str
    fecha_descarga: datetime