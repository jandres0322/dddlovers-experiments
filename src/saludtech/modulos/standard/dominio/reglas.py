from saludtech.seedwork.dominio.reglas import ReglaNegocio

from .objetos_valor import FormatoArchivo

class ValidarFormatoDescarga(ReglaNegocio):
    
  formato: str

  def __init__(self, formato, mensaje="El formato de descarga debe ser DICOM o JSON."):
    super().__init__(mensaje)
    self.formato = formato

  def es_valido(self) -> bool:
    return self.formato in [FormatoArchivo.DICOM.value, FormatoArchivo.JSON.value]
