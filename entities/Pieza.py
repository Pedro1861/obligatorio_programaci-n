class Pieza():
    def __init__(self,codigo_pieza,descripcion,costo,cantidad,lote,reposiciones=[]):
        self.codigo=codigo_pieza
        self.desc=descripcion
        self.costo=costo
        self.cantidad=cantidad
        self.lote=lote
        self.reposicion=reposiciones