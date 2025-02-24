class ProcesoMixin:
    def validar_estado(self):
        if not hasattr(self, 'estado'):
            raise AttributeError("El objeto no tiene un estado definido.")
