class Maquina():
    contador_maquina=0
    def __init__(self,descripcion,requerimiento):
        self.codigo=Maquina.contador_maquina
        Maquina.contador_maquina+=1
        self.requerimiento=requerimiento
        self.desc=descripcion

    def disponibilidad(self,disponible):
        if self.cantidad>=disponible:
            return True
        else:
            return False
        
    def agregar_requerimiento(self,nuevo_req):
        self.requerimiento.append(nuevo_req)
    
    def costo_produccion(self):
        self.requerimiento
        
