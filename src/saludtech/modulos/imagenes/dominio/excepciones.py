from saludtech.seedwork.dominio.excepciones import ExcepcionDominio

class ImagenNoEncontradaError(ExcepcionDominio):
    def __init__(self, id_imagen):
        super().__init__(f"La imagen con ID {id_imagen} no fue encontrada.")
