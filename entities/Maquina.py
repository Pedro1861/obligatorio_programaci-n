class Maquina():
    contador_maquina=0
    def __init__(self, descripcion, requerimiento=None):
        self.__codigo = Maquina.contador_maquina
        Maquina.contador_maquina += 1
        self.__requerimiento = requerimiento if requerimiento is not None else []
        self.__desc = descripcion

    @property
    def codigo(self):
        return self.__codigo

    @property
    def requerimiento(self):
        return self.__requerimiento

    @property
    def desc(self):
        return self.__desc
    def disponibilidad(self,disponible):
        if self.__cantidad>=disponible:
            return True
        else:
            return False
        
    def agregar_requerimiento(self,nuevo_req):
        self.__requerimiento.append(nuevo_req)
    
    def costo_produccion(self):
        costo=0
        for i in self.requerimiento:
            costo+=i.cantidad*i.pieza.costo
        return costo
        
