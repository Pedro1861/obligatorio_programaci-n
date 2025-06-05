from datetime import datetime

class Pedido:
    def __init__(self, cliente, maquina, fecha_recibido, fecha_entregado, estado, precio):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_recibido = fecha_recibido
        self.__fecha_entregado = fecha_entregado
        self.__estado = estado
        self.__precio = precio

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

    @property
    def estado(self):
        return self.__estado

    @property
    def precio(self):
        return self.__precio

    def get_precio(self):
        return self.__precio
    
    # NO SE COMO HACER PARA SEPARAR CLIENTE INDIVIDUAL DE EMPRESA, 
    # PORQUE SI ES INDIVIDUAL ES COSTO DE VENTA * 1.5 (EL COSTO DE VENTA +50%) 
    # Y SI ES EMPRESA ES EL PRECIO (COSTO DE VENTA * 1.5) * 0.8 
    # QUE SERIA EL 20% DE DESCUENTO POR SER EMPRESA
     
    
        
