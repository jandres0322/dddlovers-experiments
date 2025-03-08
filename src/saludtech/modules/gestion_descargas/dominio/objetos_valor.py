from enum import Enum

class EstadoDescarga(Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN_PROCESO"
    COMPLETADA = "COMPLETADA"
    FALLIDA = "FALLIDA"
    
class FormatoDescarga(Enum):
    DICOM = "DICOM"
    JSON = "JSON" 