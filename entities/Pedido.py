from datetime import datetime

class Pedido:
    def __init__(self, cliente, maquina, fecha_recibido, fecha_entregado, estado):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_recibido = fecha_recibido
        self.__fecha_entregado = fecha_entregado
        self.__estado = estado


    @property
    def cliente(self):
        return self.__cliente

    @property
    def maquina(self):
        return self.__maquina

    @property
    def fecha_recibido(self):
        return self.__fecha_recibido

    @property
    def fecha_entregado(self):
        return self.__fecha_entregado
    @fecha_entregado.setter
    def fecha_entregado(self, value):
        self.__fecha_entregado = value

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        self.__estado = value
        
    def get_precio(self):
        precio=self.__maquina.costo_produccion()
        if self.__cliente.cedula:
            precio*=1.5
        elif self.__cliente.RUT:
            precio*=1.5*0.8 
        return precio
     
    
        
