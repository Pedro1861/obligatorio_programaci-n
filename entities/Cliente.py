from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, telefono, correo_electrónico):
        self.telefono=telefono
        self.correo_electrónico=correo_electrónico
    
class ClienteParticular(Cliente):
    def __init__(self,cédula,nombre, telefono, correo_electrónico):
        super().__init__(telefono, correo_electrónico)
        self.cédula=cédula
        self.nombre=nombre

class Empresa(Cliente):
    def __init__(self,RUT,nombre, telefono, correo_electrónico):
        super().__init__(telefono, correo_electrónico)
        self.RUT=RUT
        self.nombre=nombre
