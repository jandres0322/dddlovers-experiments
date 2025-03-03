from datetime import datetime

from saludtech.seedwork.dominio.reglas import ReglaNegocio

from .objetos_valor import FormatoDescarga

class FormatoDescargaValido(ReglaNegocio):
  
  def __init__(self, formato: FormatoDescarga):
    self.formato = formato
    
  def es_valido(self):
    return self.formato in {"JSON", "DICOM"}
  
  def mensaje_error(self):
    return f"Formato de descarga inválido: {self.formato.formato}"
  
class FechaSolicitudValida(ReglaNegocio):

    def __init__(self, fecha_solicitud: datetime):
        self.fecha_solicitud = fecha_solicitud

    def es_valido(self):
        return self.fecha_solicitud <= datetime.now()

    def mensaje_error(self):
        return "La fecha de solicitud no puede ser en el futuro."