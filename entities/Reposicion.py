from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.__pieza = pieza
        self.__cantidad_lotes = cantidad_lotes
        self.__fecha = datetime.today()
        
    @property
    def pieza(self):
        return self.__pieza

    @property
    def cantidad_lotes(self):
        return self.__cantidad_lotes

    @property
    def fecha(self):
        return self.__fecha

    def get_costo(self):
        return self.__pieza.costo * self.__pieza.lote * self.__cantidad_lotes
        