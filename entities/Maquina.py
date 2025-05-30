class Maquina():
    def __init__(self,codigo_maquina,descripcion,requerimiento):
        self.codigo=codigo_maquina
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
        
