class Requerimiento():
    def __init__(self,maquina,pieza,cantidad):
        self.__pieza=pieza
        self.__maquina=maquina.codigo
        self.__cantidad=cantidad
    @property
    def pieza(self):
        return self.__pieza
    
    @property
    def maquina(self):
        return self.__maquina
    
    @property
    def cantidad(self):
        return self.__cantidad