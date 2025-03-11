from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class DTO():
    ...

class Mapeador(ABC):
    @abstractmethod
    def externo_a_dto(self, externo: any) -> DTO:
        ...

    @abstractmethod
    def dto_a_externo(self, dto: DTO) -> any:
        ...

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: str
    metadata: str
    formato: str
    base64: str

@dataclass(frozen=True)
class ArchivoDTO(DTO):
    imagenes: list[ImagenDTO]