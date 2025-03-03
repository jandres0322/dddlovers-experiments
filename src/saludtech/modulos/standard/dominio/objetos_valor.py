from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class EstadoSolicitud(Enum):
  PENDIENTE = "PENDIENTE"
  PROCESANDO = "PROCESANDO"
  PROCESADO = "PROCESADO"
  ERROR = "ERROR"

@dataclass(frozen=True)
class FormatoDescarga:
  valor: str
