class Pieza:
    contador_pieza = 0

    def __init__(self, descripcion, costo, cantidad, lote, reposiciones=None):
        if reposiciones is None:
            reposiciones = []
        self.__codigo = Pieza.contador_pieza
        Pieza.contador_pieza += 1
        self.__desc = descripcion
        self.__costo = costo
        self.__cantidad = cantidad
        self.__lote = lote
        self.__reposicion = reposiciones

    @property
    def codigo(self):
        return self.__codigo

    @property
    def desc(self):
        return self.__desc

    @property
    def costo(self):
        return self.__costo

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value
    @property
    def lote(self):
        return self.__lote

    @property
    def reposicion(self):
        return self.__reposicion
    def agregar_reposicion(self, reposicion):
        if reposicion not in self.__reposicion:
            self.__reposicion.append(reposicion)