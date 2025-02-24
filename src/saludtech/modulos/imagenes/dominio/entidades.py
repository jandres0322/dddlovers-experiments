from dataclasses import dataclass
from datetime import datetime
from .objetos_valor import EstadoImagen, EstadosImagen, MetadatosImagen
from seedwork.dominio.entidades import Entidad

@dataclass
class ImagenMedica(Entidad):
    id: str
    nombre_archivo: str
    formato: str  # Ejemplo: JSON, DICOM
    fecha_creacion: datetime
    estado: EstadoImagen
    metadatos: MetadatosImagen

    def marcar_como_procesada(self):
        self.estado = EstadoImagen(EstadosImagen.PROCESADA)
