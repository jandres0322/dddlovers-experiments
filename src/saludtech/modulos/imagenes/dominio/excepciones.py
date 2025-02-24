from saludtech.seedwork.dominio.excepciones import ExcepcionDominio, ReglaNegocioExcepcion

class ImagenNoEncontrada(ExcepcionDominio):
    def __init__(self, id_imagen: str):
        super().__init__(f"No se encontró la imagen con ID {id_imagen}.")

class FormatoNoPermitido(ReglaNegocioExcepcion):
    def __init__(self, formato: str):
        super().__init__(f"El formato '{formato}' no está permitido. Formatos válidos: DICOM, PNG, JPG.")

class TamanioExcedido(ReglaNegocioExcepcion):
    def __init__(self, tamanio: int, limite: int = 50 * 1024 * 1024):  # 50MB
        super().__init__(f"El tamaño de la imagen ({tamanio} bytes) excede el límite permitido de {limite} bytes.")

class EstadoInvalido(ExcepcionDominio):
    def __init__(self, estado: str):
        super().__init__(f"El estado '{estado}' no es válido para la imagen médica.")
