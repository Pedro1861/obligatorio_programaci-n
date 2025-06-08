from abc import ABC, abstractmethod

class Cliente(ABC):
    contador_clientes = 0

    def __init__(self, telefono, correo_electronico):
        self.__telefono = telefono
        self.__id = Cliente.contador_clientes
        Cliente.contador_clientes += 1
        self.__correo_electronico = correo_electronico

    @property
    def telefono(self):
        return self.__telefono

    @property
    def id(self):
        return self.__id

    @property
    def correo_electronico(self):
        return self.__correo_electronico

class ClienteParticular(Cliente):
    def __init__(self, cedula, nombre, telefono, correo_electronico):
        super().__init__(telefono, correo_electronico)
        self.__cedula = cedula
        self.__nombre = nombre

    @property
    def cedula(self):
        return self.__cedula

    @property
    def nombre(self):
        return self.__nombre

class Empresa(Cliente):
    def __init__(self, RUT, nombre, telefono, correo_electronico, web):
        super().__init__(telefono, correo_electronico)
        self.__RUT = RUT
        self.__nombre = nombre
        self.__web = web

    @property
    def RUT(self):
        return self.__RUT

    @property
    def nombre(self):
        return self.__nombre

    @property
    def web(self):
        return self.__web