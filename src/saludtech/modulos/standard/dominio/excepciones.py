from saludtech.seedwork.dominio.excepciones import ExcepcionDominio

class TipoObjetoNoExisteEnDominioStandardExcepcion(ExcepcionDominio):
  def __init__(self, mensaje= 'El tipo de objeto no existe en el dominio de Standard'):
    self.mensaje = mensaje
    
  def __str__(self):
    return str(self.mensaje)
