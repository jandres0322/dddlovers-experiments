from dataclasses import dataclass, field
from enum import Enum

from saludtech.seedwork.dominio.objetos_valor import ObjetoValor

class EstadoDescarga(Enum):
  PENDIENTE = 'PENDIENTE'
  LISTA = 'LISTA'
  COMPLETADA = 'COMPLETADA'
  
class FormatoArchivo(Enum):
  DICOM = 'DICOM'
  JSON = 'JSON'