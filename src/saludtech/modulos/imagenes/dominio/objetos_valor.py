from dataclasses import dataclass
from enum import Enum

class EstadoImagen(Enum):
    PENDIENTE = "pendiente"
    PROCESADA = "procesada"
    ERROR = "error"

@dataclass(frozen=True)
class MetadatosImagen:
    tamano_mb: float
    resolucion: str
    origen: str  
    fecha_captura: str  
    tipo_estudio: str

class FormatosPermitidos(Enum):
    DICOM = "dicom"
    PNG = "png"
    JPG = "jpg"