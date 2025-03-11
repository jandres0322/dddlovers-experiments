from dataclasses import field, dataclass
from saludtech.seedwork.aplicacion.dto import DTO
from typing import List


@dataclass(frozen=True)
class ObtenerImagenesDTO(DTO):
    id_solicitud: str = field(default_factory=str)
    id_imagenes: List[str] = field(default_factory=list)

class ImagenMedicaDTO(DTO):
    id: str = field(default_factory=str)
    ruta_storage: str = field(default_factory=str)
    ruta_thumbanil: str = field(default_factory=str)
    ruta_metadatos: str = field(default_factory=str)