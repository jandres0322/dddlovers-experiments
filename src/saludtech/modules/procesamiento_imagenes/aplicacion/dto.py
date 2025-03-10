from dataclasses import field, dataclass
from saludtech.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class ObtenerImagenesDTO(DTO):
    id_solicitud = str = field(default_factory=str)
    id_imagenes = list[str] = field(default_factory=list)