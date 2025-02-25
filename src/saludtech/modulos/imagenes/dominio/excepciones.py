from seedwork.dominio.excepciones import ExcepcionDominio

class ImagenNoDisponible(ExcepcionDominio):

    def __init__(self, id_imagen: str):
        super().__init__(f"La imagen con ID {id_imagen} no está disponible para entrega.")

class DescargaNoRegistrada(ExcepcionDominio):

    def __init__(self, id_entrega: str):
        super().__init__(f"No hay descargas registradas para la entrega con ID {id_entrega}.")
