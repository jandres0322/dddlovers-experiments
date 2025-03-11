from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio


class RepositorioImagenesProcesada(Repositorio, ABC):
  
    def obtener_por_id(self, id):
        return super().obtener_por_id(id)
  
    def obtener_todos(self):
        return super().obtener_todos()
    

    def agregar(self, entity):
        return super().agregar(entity)
    
    def actualizar(self, entity):
        return super().actualizar(entity)
    
    def eliminar(self, entity_id):
        return super().eliminar(entity_id)