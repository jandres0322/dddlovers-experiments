from saludtech.seedwork.dominio.reglas import ReglaNegocio


class ValidarFormatoDescarga(ReglaNegocio):
    
    formato: str
    
    def __init__(self, formato, mensaje= 'Formato no permitido'):
        super().__init__(mensaje)
        self.formato = formato
        
    def es_valido(self):
        if self.formato in ['JSON', 'DICOM']:
            return True
        return False
    
class ValidarListaImagenes(ReglaNegocio):
    
    imagenes: list[str]
    
    def __init__(self, imagenes, mensaje= 'Lista de imagenes vacia'):
        super().__init__(mensaje)
        self.imagenes = imagenes
        
    def es_valido(self):
        if len(self.imagenes) > 0:
            return True
        return False