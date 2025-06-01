from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.today()
        
    def get_costo(self):
        return self.pieza.costo*self.pieza.lote*self.cantidad_lotes
        