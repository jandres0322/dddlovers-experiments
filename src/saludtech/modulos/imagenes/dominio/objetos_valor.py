from dataclasses import dataclass
from enum import Enum

class EstadosImagen(Enum):
    PENDIENTE = "pendiente"
    PROCESADA = "procesada"
    ERROR = "error"

@dataclass(frozen=True)
class EstadoImagen:
    estado: EstadosImagen

    def es_procesada(self) -> bool:
        return self.estado == EstadosImagen.PROCESADA

    def es_pendiente(self) -> bool:
        return self.estado == EstadosImagen.PENDIENTE

    def es_error(self) -> bool:
        return self.estado == EstadosImagen.ERROR

@dataclass(frozen=True)
class MetadatosImagen:
    tamano_mb: float
    resolucion: str
    origen: str  
    fecha_captura: str  
    tipo_estudio: str
