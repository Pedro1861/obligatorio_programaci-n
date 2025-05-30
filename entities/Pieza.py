class Pieza():
    contador_pieza=0
    def __init__(self,descripcion,costo,cantidad,lote,reposiciones=[]):
        self.codigo=Pieza.contador_pieza
        Pieza.contador_pieza+=1
        self.desc=descripcion
        self.costo=costo
        self.cantidad=cantidad
        self.lote=lote
        self.reposicion=reposiciones